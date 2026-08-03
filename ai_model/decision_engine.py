class DecisionEngine:
    """
    Главный модуль принятия решений

    Объединяет:
    - AI сигнал
    - риск
    - режим рынка
    - торговые ограничения

    Выдает:
    - BUY
    - SELL
    - HOLD
    """

    def __init__(
        self,
        min_confidence=60
    ):

        self.min_confidence = min_confidence



    def analyze(
        self,
        ai_signal,
        confidence,
        market_regime,
        risk_allowed=True
    ):


        # Проверка риска

        if not risk_allowed:

            return {

                "decision": "HOLD",

                "reason":
                    "Risk manager blocked"

            }



        # Слабый сигнал

        if confidence < self.min_confidence:

            return {

                "decision": "HOLD",

                "reason":
                    "Low AI confidence"

            }



        # Фильтр рынка


        if market_regime == "HIGH_VOLATILITY":


            if confidence < 80:

                return {

                    "decision": "HOLD",

                    "reason":
                        "High volatility protection"

                }



        # Принятие решения


        if ai_signal == "LONG":

            return {

                "decision": "BUY",

                "confidence":
                    confidence,

                "reason":
                    "AI consensus LONG"

            }



        elif ai_signal == "SHORT":

            return {

                "decision": "SELL",

                "confidence":
                    confidence,

                "reason":
                    "AI consensus SHORT"

            }



        else:

            return {

                "decision": "HOLD",

                "reason":
                    "No clear signal"

            }