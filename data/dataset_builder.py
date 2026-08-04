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
from indicators.adx import calculate_adx
from indicators.atr import calculate_atr
from indicators.bollinger import calculate_bollinger_bands



class DatasetBuilder:


    def build(
        self,
        filename="data/history.csv"
    ):


        df = pd.read_csv(filename)


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

        df["MACD_signal"] = signal_line

        df["MACD_hist"] = histogram



        df["ADX"] = calculate_adx(
            df,
            14
        )


        df["ATR"] = calculate_atr(
            df,
            14
        )



        upper, middle, lower = calculate_bollinger_bands(
            df
        )


        df["BB_upper"] = upper

        df["BB_middle"] = middle

        df["BB_lower"] = lower



        future_price = df["close"].shift(-1)


        # TARGET
        # 1 = рост
        # 0 = падение

        df["target"] = 0


        df.loc[
            future_price > df["close"],
            "target"
        ] = 1



        df = df.dropna()



        df.to_csv(
            "data/training_dataset.csv",
            index=False
        )


        print("==============================")
        print("TRAINING DATASET CREATED")
        print("Rows:", len(df))
        print(list(df.columns))
        print("==============================")



if __name__ == "__main__":

    builder = DatasetBuilder()

    builder.build()