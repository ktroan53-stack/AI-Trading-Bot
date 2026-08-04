from ai_model.predictor import AIPredictor



class AIEnsemble:
    """
    AI Ensemble Engine v0.2

    Объединяет:
    - ML модели
    - технические признаки
    - прогнозы AI
    """


    def __init__(self, model_path=None):

        self.models = []

        self.predictor = AIPredictor(
            model_path
        )



    def add_model(self, model):

        self.models.append(
            model
        )



    def predict(self, features):


        if features is None or len(features) == 0:

            return {

                "signal": "HOLD",

                "confidence": 0,

                "probability": 0

            }



        predictions = []



        # =========================
        # ML MODEL
        # =========================

        ml_prediction = self.predictor.predict(
            features.iloc[-1]
        )


        predictions.append(
            ml_prediction
        )



        # =========================
        # ADDITIONAL MODELS
        # =========================

        for model in self.models:


            prediction = model.predict(
                features
            )


            predictions.append(
                prediction
            )



        buy_score = 0

        sell_score = 0



        total_confidence = 0



        for prediction in predictions:


            confidence = prediction.get(
                "confidence",
                0
            )


            signal = prediction.get(
                "signal"
            )


            if signal == "BUY":

                buy_score += confidence


            elif signal == "SELL":

                sell_score += confidence



            total_confidence += confidence



        # =========================
        # FINAL AI DECISION
        # =========================


        if buy_score > sell_score:

            return {

                "signal": "BUY",

                "confidence":
                    round(
                        buy_score /
                        max(
                            len(predictions),
                            1
                        ),
                        2
                    ),

                "probability":
                    round(
                        buy_score /
                        max(
                            total_confidence,
                            1
                        ),
                        3
                    )

            }



        if sell_score > buy_score:

            return {

                "signal": "SELL",

                "confidence":
                    round(
                        sell_score /
                        max(
                            len(predictions),
                            1
                        ),
                        2
                    ),

                "probability":
                    round(
                        sell_score /
                        max(
                            total_confidence,
                            1
                        ),
                        3
                    )

            }



        return {

            "signal": "HOLD",

            "confidence": 50,

            "probability": 0.5

        }