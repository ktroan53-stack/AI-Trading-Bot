class AIRiskManager:
    """
    AI отдел управления рисками

    Анализирует:
    - уверенность AI
    - волатильность
    - режим рынка
    - стиль торговли

    Выдает:
    - разрешение сделки
    - размер риска
    - коэффициент агрессии
    """

    def __init__(
        self,
        mode="BALANCED"
    ):

        self.mode = mode


        self.settings = {

            "CONSERVATIVE": {

                "max_risk": 0.01,
                "min_confidence": 75

            },


            "BALANCED": {

                "max_risk": 0.02,
                "min_confidence": 65

            },


            "AGGRESSIVE": {

                "max_risk": 0.03,
                "min_confidence": 55

            }

        }



    def analyze(
        self,
        confidence,
        market_regime,
        drawdown=0
    ):


        settings = self.settings[self.mode]


        risk = settings["max_risk"]



        # Проверка уверенности

        if confidence < settings["min_confidence"]:

            return {

                "allowed": False,

                "risk": 0,

                "reason":
                    "AI confidence too low"

            }



        # Защита при высокой волатильности

        if market_regime == "HIGH_VOLATILITY":

            risk *= 0.5



        # Защита при просадке

        if drawdown > 10:

            risk *= 0.5



        if drawdown > 20:

            return {

                "allowed": False,

                "risk": 0,

                "reason":
                    "Maximum drawdown protection"

            }



        return {

            "allowed": True,

            "risk":
                round(
                    risk,
                    4
                ),

            "mode":
                self.mode,

            "reason":
                "Risk approved"

        }



    def change_mode(
        self,
        mode
    ):

        if mode in self.settings:

            self.mode = mode