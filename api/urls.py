from django.urls import path

from .views import call_rpc_method

urlpatterns = [
    path('call/', call_rpc_method, name='call_rpc_method'),
]
