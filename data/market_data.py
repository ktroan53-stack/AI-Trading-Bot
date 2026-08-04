import requests
import pandas as pd

from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd
from indicators.bollinger import calculate_bollinger_bands
from indicators.atr import calculate_atr
from indicators.adx import calculate_adx



BINANCE_URL = "https://api.binance.com/api/v3/klines"



def load_candles(
    symbol="BTCUSDT",
    interval="1h",
    limit=100
):

    params = {

        "symbol": symbol,

        "interval": interval,

        "limit": limit

    }


    response = requests.get(
        BINANCE_URL,
        params=params
    )


    data = response.json()



    candles = []


    for candle in data:

        candles.append(

            {

                "time": candle[0],

                "open": float(candle[1]),

                "high": float(candle[2]),

                "low": float(candle[3]),

                "close": float(candle[4]),

                "volume": float(candle[5])

            }

        )



    df = pd.DataFrame(
        candles
    )



    # =====================
    # INDICATORS
    # =====================


    df["EMA20"] = calculate_ema(
        df,
        20
    )


    df["EMA50"] = calculate_ema(
        df,
        50
    )


    df["RSI14"] = calculate_rsi(
        df,
        14
    )



    macd_line, signal_line, histogram = calculate_macd(
        df
    )


    df["MACD"] = macd_line

    df["MACD_SIGNAL"] = signal_line

    df["MACD_HIST"] = histogram



    upper, middle, lower = calculate_bollinger_bands(
        df
    )


    df["BB_UPPER"] = upper

    df["BB_MIDDLE"] = middle

    df["BB_LOWER"] = lower



    df["ATR"] = calculate_atr(
        df,
        14
    )


    df["ADX"] = calculate_adx(
        df,
        14
    )



    return df