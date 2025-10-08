from django.urls import path
from core.consumers import LiveStockConsumer

websocket_urlpatterns = [
    path("ws/stocks/", LiveStockConsumer.as_asgi()),
]


