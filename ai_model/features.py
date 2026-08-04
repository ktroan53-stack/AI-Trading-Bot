import pandas as pd


class FeatureBuilder:
    """
    Формирование признаков для AI моделей

    Подготовка данных для:
    - XGBoost
    - LightGBM
    - Random Forest
    - Neural Networks

    Версия:
    Feature Engine v0.2
    """

    def __init__(self):
        pass


    def create_features(self, df):

        data = df.copy()


        # =========================
        # PRICE FEATURES
        # =========================

        # Изменение цены

        data["price_change"] = (
            data["close"]
            .pct_change()
        )


        # Доходность за период

        data["momentum_10"] = (
            data["close"]
            -
            data["close"].shift(10)
        )


        # =========================
        # VOLATILITY FEATURES
        # =========================

        # Волатильность

        data["volatility"] = (
            data["close"]
            .rolling(20)
            .std()
        )


        # ATR относительно цены

        if "ATR" in data.columns:

            data["atr_normalized"] = (
                data["ATR"]
                /
                data["close"]
            )


        # =========================
        # CANDLE FEATURES
        # =========================

        # Размер свечи

        data["candle_size"] = (
            data["high"]
            -
            data["low"]
        )


        # Направление свечи

        data["candle_direction"] = (
            data["close"]
            -
            data["open"]
        )


        # =========================
        # VOLUME FEATURES
        # =========================

        if "volume" in data.columns:

            data["volume_change"] = (
                data["volume"]
                .pct_change()
            )


        # =========================
        # TREND FEATURES
        # =========================

        if "EMA20" in data.columns:

            data["ema20_distance"] = (
                data["close"]
                -
                data["EMA20"]
            ) / data["close"]


        if "EMA50" in data.columns:

            data["ema50_distance"] = (
                data["close"]
                -
                data["EMA50"]
            ) / data["close"]


        # =========================
        # RSI
        # =========================

        if "RSI14" in data.columns:

            data["rsi_normalized"] = (
                data["RSI14"]
                /
                100
            )


        # =========================
        # MACD
        # =========================

        if (
            "MACD" in data.columns
            and
            "MACD_SIGNAL" in data.columns
        ):

            data["macd_difference"] = (
                data["MACD"]
                -
                data["MACD_SIGNAL"]
            )


        # =========================
        # ADX TREND STRENGTH
        # =========================

        if "ADX" in data.columns:

            data["adx_strength"] = (
                data["ADX"]
                /
                100
            )


        # =========================
        # BOLLINGER POSITION
        # =========================

        if (
            "BB_UPPER" in data.columns
            and
            "BB_LOWER" in data.columns
        ):

            data["bb_position"] = (

                (
                    data["close"]
                    -
                    data["BB_LOWER"]
                )
                /
                (
                    data["BB_UPPER"]
                    -
                    data["BB_LOWER"]
                )

            )


        # =========================
        # CLEAN DATA
        # =========================

        data = (
            data
            .replace(
                [
                    float("inf"),
                    -float("inf")
                ],
                None
            )
            .dropna()
        )


        return data