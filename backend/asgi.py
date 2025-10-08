"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from core.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')



application=ProtocolTypeRouter({

    'http':get_asgi_application(),   # For normal HTTP requests

    "websocket":AuthMiddlewareStack(        
        URLRouter(
            websocket_urlpatterns)   # For WebSocket connections
        ),

})