import pandas as pd
import numpy as np

from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd
from indicators.bollinger import calculate_bollinger_bands
from indicators.atr import calculate_atr
from indicators.adx import calculate_adx


def load_candles():

    np.random.seed(42)

    prices = []

    price = 64000


    # Генерируем 100 тестовых свечей

    for i in range(100):

        change = np.random.randint(
            -500,
            500
        )

        price += change

        prices.append(price)



    df = pd.DataFrame(
        {
            "close": prices
        }
    )


    df["open"] = df["close"].shift(1)


    df["high"] = (
        df["close"]
        +
        np.random.randint(
            100,
            500,
            100
        )
    )


    df["low"] = (
        df["close"]
        -
        np.random.randint(
            100,
            500,
            100
        )
    )


    # =====================
    # EMA
    # =====================

    df["EMA20"] = calculate_ema(
        df,
        20
    )


    df["EMA50"] = calculate_ema(
        df,
        50
    )



    # =====================
    # RSI
    # =====================

    df["RSI14"] = calculate_rsi(
        df,
        14
    )



    # =====================
    # MACD
    # =====================

    macd_line, signal_line, histogram = calculate_macd(
        df
    )


    df["MACD"] = macd_line

    df["MACD_SIGNAL"] = signal_line

    df["MACD_HIST"] = histogram



    # =====================
    # Bollinger Bands
    # =====================

    upper, middle, lower = calculate_bollinger_bands(
        df
    )


    df["BB_UPPER"] = upper

    df["BB_MIDDLE"] = middle

    df["BB_LOWER"] = lower



    # =====================
    # ATR
    # =====================

    df["ATR"] = calculate_atr(
        df,
        14
    )



    # =====================
    # ADX
    # =====================

    df["ADX"] = calculate_adx(
        df,
        14
    )



    return df