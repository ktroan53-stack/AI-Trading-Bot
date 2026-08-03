class AIEnsemble:
    """
    Объединение нескольких AI моделей

    Источники:
    - XGBoost
    - LightGBM
    - технический анализ
    - другие модели в будущем

    Возвращает:
    - общий сигнал
    - уверенность
    """

    def __init__(self):

        self.predictions = []



    def add_prediction(
        self,
        model_name,
        signal,
        confidence
    ):

        self.predictions.append({

            "model":
                model_name,

            "signal":
                signal,

            "confidence":
                confidence

        })



    def calculate_consensus(self):

        if len(self.predictions) == 0:

            return {

                "signal": "HOLD",

                "confidence": 0

            }


        long_score = 0
        short_score = 0
        hold_score = 0



        for prediction in self.predictions:

            confidence = (
                prediction["confidence"]
                /
                100
            )


            if prediction["signal"] == "LONG":

                long_score += confidence


            elif prediction["signal"] == "SHORT":

                short_score += confidence


            else:

                hold_score += confidence



        scores = {

            "LONG": long_score,

            "SHORT": short_score,

            "HOLD": hold_score

        }



        final_signal = max(
            scores,
            key=scores.get
        )


        total = sum(
            scores.values()
        )


        if total == 0:

            confidence = 0

        else:

            confidence = (
                scores[final_signal]
                /
                total
                *
                100
            )


        return {

            "signal":
                final_signal,

            "confidence":
                round(
                    confidence,
                    2
                ),

            "details":
                scores

        }



    def clear(self):

        self.predictions = []