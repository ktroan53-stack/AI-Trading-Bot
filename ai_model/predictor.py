import os
import pickle
import pandas as pd


class AIPredictor:


    def __init__(
        self,
        model_path="ai_model/models/xgboost_v1.pkl"
    ):

        self.model_path = model_path

        self.model = self.load_model()



    def load_model(self):

        if not os.path.exists(
            self.model_path
        ):

            print(
                "AI model not found"
            )

            return None


        with open(
            self.model_path,
            "rb"
        ) as file:

            return pickle.load(file)



    def predict(
        self,
        features
    ):


        if self.model is None:

            return {

                "signal": "HOLD",

                "confidence": 0,

                "probability": 0

            }



        if isinstance(
            features,
            pd.Series
        ):

            features = features.to_frame().T



        # приводим LIVE названия к формату обучения

        rename_map = {

            "MACD_SIGNAL": "MACD_signal",

            "MACD_HIST": "MACD_hist",

            "BB_UPPER": "BB_upper",

            "BB_MIDDLE": "BB_middle",

            "BB_LOWER": "BB_lower"

        }


        features = features.rename(
            columns=rename_map
        )



        required_features = [

            "time",

            "open",

            "high",

            "low",

            "close",

            "volume",

            "EMA20",

            "EMA50",

            "RSI14",

            "MACD",

            "MACD_signal",

            "MACD_hist",

            "ADX",

            "ATR",

            "BB_upper",

            "BB_middle",

            "BB_lower"

        ]



        features = features[
            required_features
        ]



        prediction = self.model.predict(
            features
        )[0]



        probability = self.model.predict_proba(
            features
        )[0]



        confidence = max(
            probability
        ) * 100



        if prediction == 1:

            signal = "BUY"

        else:

            signal = "SELL"



        return {

            "signal": signal,

            "confidence": round(
                confidence,
                2
            ),

            "probability": round(
                max(probability),
                3
            )

        }