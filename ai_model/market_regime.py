import pandas as pd


class MarketRegimeDetector:
    """
    Определение состояния рынка

    Режимы:
    - TREND_UP
    - TREND_DOWN
    - SIDEWAYS
    - HIGH_VOLATILITY
    """


    def __init__(self):
        pass


    def detect(self, df):

        last = df.iloc[-1]


        close = last["close"]

        ema20 = last.get("EMA20")
        ema50 = last.get("EMA50")

        atr = last.get("ATR")


        volatility = False
        trend_up = False
        trend_down = False


        # Проверка волатильности

        if atr is not None:

            average_atr = (
                df["ATR"]
                .rolling(50)
                .mean()
                .iloc[-1]
            )

            if atr > average_atr * 1.5:
                volatility = True



        # Проверка тренда

        if ema20 is not None and ema50 is not None:


            if ema20 > ema50 and close > ema20:

                trend_up = True


            elif ema20 < ema50 and close < ema20:

                trend_down = True



        # Определение режима


        if volatility:

            regime = "HIGH_VOLATILITY"


        elif trend_up:

            regime = "TREND_UP"


        elif trend_down:

            regime = "TREND_DOWN"


        else:

            regime = "SIDEWAYS"



        return {

            "regime": regime,

            "trend_up": trend_up,

            "trend_down": trend_down,

            "volatility": volatility

        }