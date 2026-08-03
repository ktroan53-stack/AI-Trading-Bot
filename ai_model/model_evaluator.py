import pandas as pd


class ModelEvaluator:
    """
    Оценка и сравнение AI моделей

    Задачи:
    - сравнение моделей
    - выбор лучшей версии
    - хранение результатов тестов
    """

    def __init__(self):

        self.results = []


    def add_result(
        self,
        model_name,
        accuracy,
        profit_factor,
        sharpe,
        drawdown
    ):

        result = {

            "model": model_name,

            "accuracy": accuracy,

            "profit_factor": profit_factor,

            "sharpe": sharpe,

            "drawdown": drawdown

        }

        self.results.append(result)



    def compare(self):

        if len(self.results) == 0:

            return None


        df = pd.DataFrame(
            self.results
        )


        # Итоговый рейтинг модели
        #
        # Больше:
        # accuracy
        # profit_factor
        # sharpe
        #
        # Меньше:
        # drawdown


        df["score"] = (

            df["accuracy"] * 0.25

            +

            df["profit_factor"] * 20 * 0.35

            +

            df["sharpe"] * 20 * 0.25

            -

            df["drawdown"] * 0.15

        )


        best = df.sort_values(
            "score",
            ascending=False
        ).iloc[0]


        return {

            "best_model":
                best["model"],

            "score":
                round(
                    best["score"],
                    2
                )

        }



    def report(self):

        return pd.DataFrame(
            self.results
        )