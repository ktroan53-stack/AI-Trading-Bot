import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


import pandas as pd

from indicators.ema import calculate_ema
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd
from indicators.bollinger import calculate_bollinger_bands
from indicators.atr import calculate_atr
from indicators.adx import calculate_adx

from ai_model.features import FeatureBuilder



def build_dataset():


    print("==============================")
    print("BUILDING DATASET v3")
    print("==============================")


    df = pd.read_csv(
        "data/history.csv"
    )


    print(
        "Loaded:",
        len(df)
    )



    # EMA

    df["EMA20"] = calculate_ema(
        df,
        20
    )


    df["EMA50"] = calculate_ema(
        df,
        50
    )


    df["EMA200"] = calculate_ema(
        df,
        200
    )



    # RSI

    df["RSI14"] = calculate_rsi(
        df,
        14
    )



    # MACD

    macd, signal, hist = calculate_macd(
        df
    )


    df["MACD"] = macd

    df["MACD_SIGNAL"] = signal

    df["MACD_HIST"] = hist



    # Bollinger

    upper, middle, lower = calculate_bollinger_bands(
        df
    )


    df["BB_UPPER"] = upper

    df["BB_MIDDLE"] = middle

    df["BB_LOWER"] = lower



    # ATR

    df["ATR"] = calculate_atr(
        df,
        14
    )



    # ADX

    df["ADX"] = calculate_adx(
        df,
        14
    )



    # TARGET

    df["target"] = 0


    future = df["close"].shift(-10)


    df.loc[
        future > df["close"] * 1.01,
        "target"
    ] = 1


    df.loc[
        future < df["close"] * 0.99,
        "target"
    ] = -1



    # AI FEATURES

    builder = FeatureBuilder()


    df = builder.create_features(
        df
    )



    df.to_csv(
        "data/training_dataset_v3.csv",
        index=False
    )



    print("==============================")
    print("DATASET CREATED")
    print(
        "Rows:",
        len(df)
    )

    print(
        df.columns.tolist()
    )

    print("==============================")



if __name__ == "__main__":

    build_dataset()