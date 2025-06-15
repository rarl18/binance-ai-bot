
import os
from binance.client import Client

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")
client = Client(api_key, api_secret)

def get_klines(symbol="BTCUSDT", interval="15m", limit=100):
    klines = client.futures_klines(symbol=symbol, interval=interval, limit=limit)
    import pandas as pd
    df = pd.DataFrame(klines, columns=[
        'timestamp','open','high','low','close','volume','close_time','quote_asset_volume',
        'num_trades','taker_buy_base','taker_buy_quote','ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    df = df.astype(float)
    return df
