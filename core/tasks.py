from celery import shared_task
import redis
import yfinance as yf
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#synctronous redis client
redis_client = redis.StrictRedis.from_url("redis://127.0.0.1:6379/2")
channel_layer = get_channel_layer()

@shared_task
def fetch_stocks_task(symbols,channel_name):
    results={}

    for symbol in symbols:
        cached=redis_client.get(symbol)
        if cached:
            results[symbol]=float(cached)
            continue    

        ticker=yf.Ticker(symbol)
        price=ticker.info.get("regularMarketPrice")
        if price is not None:
            redis_client.set(symbol,price,ex=10)
        results[symbol]=price


    async_to_sync(channel_layer.send)(channel_name,{
        "type":"send_stock_update",
        "data":results
    })

    return results