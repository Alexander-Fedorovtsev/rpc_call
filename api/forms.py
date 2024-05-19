from django import forms


class RpcMethodForm(forms.Form):
    endpoint = forms.URLField(label='Endpoint', initial='https://slb.medv.ru/api/v2/')
    method = forms.CharField(label='Method', max_length=100, initial='auth.check')
    params = forms.CharField(label='Params', widget=forms.Textarea, required=False)
