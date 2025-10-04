from celery import shared_task
import redis.asyncio as redis
import asyncio
import yfinance as yf
from channels.layers import get_channel_layer

REDIS_URL = "redis://127.0.0.1:6379/2"
redis_client = redis.from_url(REDIS_URL)
channel_layer = get_channel_layer()

@shared_task
def fetch_stocks_task(symbols, channel_name):
    async def fetch_symbol(symbol):
        cached = await redis_client.get(symbol)
        if cached:
            return float(cached)
        def fetch():
            ticker = yf.Ticker(symbol)
            return ticker.info.get("regularMarketPrice")
        price = await asyncio.to_thread(fetch)
        if price is not None:
            await redis_client.set(symbol, price, ex=10)
        return price

    async def main():
        results = await asyncio.gather(*[fetch_symbol(sym) for sym in symbols])
        data = {sym: price for sym, price in zip(symbols, results)}
        await channel_layer.send(channel_name, {
            "type": "send_stock_update",
            "data": data
        })

    asyncio.run(main())
