import requests
import pandas as pd

from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi


def load_candles(symbol="BTCUSDT", interval="1h", limit=500):

    url = (
        f"https://api.binance.com/api/v3/klines"
        f"?symbol={symbol}&interval={interval}&limit={limit}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    candles = response.json()

    df = pd.DataFrame(
        candles,
        columns=[
            "open_time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_volume",
            "trades",
            "taker_buy_base",
            "taker_buy_quote",
            "ignore",
        ],
    )

    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    for column in numeric_columns:
        df[column] = df[column].astype(float)

    df["EMA20"] = calculate_ema(df)
    df["RSI14"] = calculate_rsi(df)

    return df