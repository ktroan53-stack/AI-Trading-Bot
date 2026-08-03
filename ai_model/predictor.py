import pickle
import pandas as pd


class AIPredictor:
    """
    Прогнозирование AI Trading Bot

    Получает:
    - подготовленные признаки

    Возвращает:
    - LONG
    - SHORT
    - HOLD
    - вероятность решения
    """

    def __init__(self, model_path):

        self.model_path = model_path
        self.model = self.load_model()


    def load_model(self):

        try:

            with open(
                self.model_path,
                "rb"
            ) as file:

                model = pickle.load(file)

            return model


        except FileNotFoundError:

            print(
                "AI модель не найдена"
            )

            return None



    def predict(self, features):

        if self.model is None:

            return {
                "signal": "HOLD",
                "confidence": 0
            }


        if isinstance(features, pd.Series):

            features = features.to_frame().T



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

            signal = "LONG"

        elif prediction == -1:

            signal = "SHORT"

        else:

            signal = "HOLD"



        return {

            "signal": signal,

            "confidence": round(
                confidence,
                2
            )

        }