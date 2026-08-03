import pandas as pd


class FeatureBuilder:
    """
    Формирование признаков для AI моделей

    Подготовка данных для:
    - XGBoost
    - LightGBM
    - Random Forest
    - Neural Networks
    """

    def __init__(self):
        pass


    def create_features(self, df):

        data = df.copy()


        # Изменение цены
        data["price_change"] = (
            data["close"]
            .pct_change()
        )


        # Волатильность
        data["volatility"] = (
            data["close"]
            .rolling(20)
            .std()
        )


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


        # Объем
        if "volume" in data.columns:

            data["volume_change"] = (
                data["volume"]
                .pct_change()
            )


        # Расстояние от EMA20
        if "EMA20" in data.columns:

            data["ema_distance"] = (
                data["close"]
                -
                data["EMA20"]
            )


        # Расстояние от EMA50
        if "EMA50" in data.columns:

            data["ema50_distance"] = (
                data["close"]
                -
                data["EMA50"]
            )


        # RSI зона
        if "RSI14" in data.columns:

            data["rsi_normalized"] = (
                data["RSI14"]
                /
                100
            )


        # Удаляем пустые значения

        data = data.dropna()


        return data
        