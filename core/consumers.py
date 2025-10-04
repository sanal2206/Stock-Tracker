import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from .tasks import fetch_stocks_task
import asyncio

class LiveStockConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.symbols = []

    async def disconnect(self, close_code):
    # Leave all symbol groups
        for symbol in getattr(self, "symbols", []):
            await self.channel_layer.group_discard(f"symbol_{symbol}", self.channel_name)


    async def receive(self, text_data):
        data = json.loads(text_data)
        symbols = data.get("symbols")
        if not symbols or not isinstance(symbols, list):
            await self.send(text_data=json.dumps({"error": "Provide a list of symbols"}))
            return

        self.symbols = symbols


        # Join groups for each symbol
        for symbol in symbols:
            await self.channel_layer.group_add(f"symbol_{symbol}", self.channel_name)

        # Start periodic Celery fetch
        asyncio.create_task(self.periodic_fetch())

    async def periodic_fetch(self):
        while True:
            # Assign Celery task for this user's symbols
            async_to_sync(fetch_stocks_task.delay)(self.symbols, self.channel_name)
            await asyncio.sleep(5)

    async def send_stock_update(self, event):
        # Receive updates from Celery
        await self.send(text_data=json.dumps(event["data"]))
