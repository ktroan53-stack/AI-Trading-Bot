class ModelSelector:
    """
    Выбор лучшей AI модели

    Анализирует:
    - результаты моделей
    - режим рынка
    - качество прогнозов

    Выбирает:
    - XGBoost
    - LightGBM
    """


    def __init__(self):

        self.models = {}

        self.performance = {}



    def register_model(
        self,
        name,
        model
    ):

        self.models[name] = model



    def update_performance(
        self,
        name,
        profit_factor,
        sharpe,
        drawdown
    ):

        score = (

            profit_factor * 0.5

            +

            sharpe * 0.3

            -

            drawdown * 0.2

        )


        self.performance[name] = {

            "score": round(
                score,
                3
            ),

            "profit_factor":
                profit_factor,

            "sharpe":
                sharpe,

            "drawdown":
                drawdown

        }



    def choose_best_model(
        self,
        market_regime
    ):


        if len(self.performance) == 0:

            return None



        best_model = max(

            self.performance,

            key=lambda x:
                self.performance[x]["score"]

        )



        return {

            "model":
                best_model,

            "market_regime":
                market_regime,

            "score":
                self.performance[best_model]["score"]

        }



    def get_models(self):

        return list(
            self.models.keys()
        )