class AIRiskManager:
    """
    AI Risk Department v0.2

    Управление риском:
    - проверка уверенности
    - режим рынка
    - защита капитала
    """


    def __init__(self, mode="BALANCED"):

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


        # Критическая блокировка только
        # при очень слабом сигнале

        if confidence < 40:

            return {

                "allowed": False,

                "risk": 0,

                "reason":
                    "Confidence critically low"

            }



        # Снижение риска во флэте

        if market_regime == "SIDEWAYS":

            risk *= 0.5



        # Высокая волатильность

        if market_regime == "HIGH_VOLATILITY":

            risk *= 0.5



        # Защита просадки

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
                round(risk,4),

            "mode":
                self.mode,

            "reason":
                "Risk approved"

        }



    def change_mode(self, mode):

        if mode in self.settings:

            self.mode = mode