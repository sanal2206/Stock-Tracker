from django.urls import path
from .consumers import LiveStockConsumer

websocket_urlpatterns = [
    path('ws/test/',LiveStockConsumer.as_asgi())
]