from django.urls import path
from . import apis

websocket_urlpatterns = [
    path(r'test/', apis.TestWS.as_asgi()),
]