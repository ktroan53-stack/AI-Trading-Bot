import pickle
import pandas as pd


class AIPredictor:
    """
    AI Predictor v0.2

    Отвечает за:
    - загрузку ML модели
    - прогноз направления
    - расчёт уверенности
    - передачу результата в AI Ensemble
    """


    def __init__(self, model_path=None):

        self.model_path = model_path

        self.model = self.load_model()



    def load_model(self):

        if self.model_path is None:

            return None


        try:

            with open(
                self.model_path,
                "rb"
            ) as file:

                return pickle.load(file)


        except FileNotFoundError:

            print(
                "AI model not found"
            )

            return None



    def predict(self, features):


        if self.model is None:

            return {

                "signal": "HOLD",

                "confidence": 0,

                "source":
                    "no_model"

            }



        if isinstance(features, pd.Series):

            features = features.to_frame().T



        prediction = self.model.predict(
            features
        )[0]


        probability = self.model.predict_proba(
            features
        )[0]


        confidence = round(
            max(probability) * 100,
            2
        )



        if prediction == 1:

            signal = "BUY"


        elif prediction == -1:

            signal = "SELL"


        else:

            signal = "HOLD"



        return {

            "signal": signal,

            "confidence": confidence,

            "probability":
                round(
                    max(probability),
                    3
                ),

            "source":
                "ML_MODEL"

        }