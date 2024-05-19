import json

from django.conf import settings
from django.shortcuts import render

from api.rpc_client import JsonRpcClient

from .forms import RpcMethodForm


def call_rpc_method(request):
    result = None
    error = None
    if request.method == 'POST':
        form = RpcMethodForm(request.POST)
        if form.is_valid():
            endpoint = form.cleaned_data['endpoint']
            method = form.cleaned_data['method']
            params = form.cleaned_data['params']
            if params:
                try:
                    params = json.loads(params)
                except json.JSONDecodeError:
                    params = {}
            client = JsonRpcClient(endpoint, settings.CLIENT_CERTIFICATE, settings.CLIENT_KEY)
            response = client.call_method(method, params)
            if 'error' in response:
                error = response['error']
            else:
                result = response
    else:
        form = RpcMethodForm()

    return render(request, 'api/call_rpc_method.html', {'form': form, 'result': result, 'error': error})
