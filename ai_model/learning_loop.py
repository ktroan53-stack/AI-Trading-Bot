from datetime import datetime


class LearningLoop:
    """
    Цикл самообучения AI Trading Bot

    Отвечает за:
    - анализ результатов моделей
    - сравнение версий
    - принятие решения об обновлении
    """

    def __init__(self):

        self.history = []


    def record_result(
        self,
        model_name,
        profit,
        sharpe,
        drawdown
    ):

        result = {

            "model": model_name,

            "profit": profit,

            "sharpe": sharpe,

            "drawdown": drawdown,

            "time":
                datetime.now()

        }


        self.history.append(result)



    def calculate_score(
        self,
        profit,
        sharpe,
        drawdown
    ):

        """
        Оценка модели

        Больше:
        прибыль
        Sharpe

        Меньше:
        просадка
        """

        score = (

            profit * 0.5

            +

            sharpe * 30 * 0.3

            -

            drawdown * 0.2

        )


        return round(
            score,
            3
        )



    def should_replace(
        self,
        old_model,
        new_model
    ):

        old_score = self.calculate_score(
            old_model["profit"],
            old_model["sharpe"],
            old_model["drawdown"]
        )


        new_score = self.calculate_score(
            new_model["profit"],
            new_model["sharpe"],
            new_model["drawdown"]
        )


        if new_score > old_score:

            return True


        return False



    def get_history(self):

        return self.history