import json
import os
import tempfile

import requests


class JsonRpcClient:
    def __init__(self, endpoint, cert_text, key_text):
        self.endpoint = endpoint
        self.cert_text = cert_text
        self.key_text = key_text

    def _create_temp_files(self):
        cert_file = tempfile.NamedTemporaryFile(delete=False, suffix='.crt')
        cert_file.write(self.cert_text.encode('utf-8'))
        cert_file.close()

        key_file = tempfile.NamedTemporaryFile(delete=False, suffix='.key')
        key_file.write(self.key_text.encode('utf-8'))
        key_file.close()

        return cert_file.name, key_file.name

    def call_method(self, method, params=None, debug=False):
        payload = {'jsonrpc': '2.0', 'method': method, 'id': 33}

        if params:
            payload['params'] = params

        headers = {
            'Content-Type': 'application/json',
        }
        if debug:
            print('Endpoint:', self.endpoint)
            print('Payload:', json.dumps(payload, indent=4))
            print('Headers:', headers)

        cert_file, key_file = self._create_temp_files()
        try:
            response = requests.post(
                self.endpoint, json=payload, headers=headers, cert=(cert_file, key_file), verify=True
            )
            response.raise_for_status()

            if debug:
                print('Response Status Code:', response.status_code)
                print('Response Headers:', response.headers)
                print('Response Text:', response.text)

            try:
                response_data = response.json()
            except json.JSONDecodeError:
                return {'error': 'Invalid JSON response', 'response_text': response.text}

            return response_data
        except requests.exceptions.HTTPError as e:
            if debug:
                print('HTTPError:', e.response.status_code, e.response.reason)
            return {
                'error': f'HTTPError: {e.response.status_code} - {e.response.reason}',
                'response_text': e.response.text,
            }
        except requests.exceptions.RequestException as e:
            print('RequestException:', str(e))
            return {'error': f'RequestException: {str(e)}'}
        except Exception as e:
            print('Unexpected error:', str(e))
            return {'error': f'Unexpected error: {str(e)}'}
        finally:
            try:
                os.remove(cert_file)
                os.remove(key_file)
            except OSError as e:
                print(f'Error deleting temp files: {e}')
