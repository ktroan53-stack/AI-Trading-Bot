class TradeErrorAnalyzer:
    """
    Анализатор убыточных сделок

    Анализирует:
    - причины убытка
    - ошибки модели
    - ошибки входа
    - рыночные условия

    Используется для:
    - улучшения AI
    - обучения новых моделей
    """


    def __init__(self):

        self.errors = []



    def analyze_trade(
        self,
        trade
    ):

        analysis = {

            "symbol":
                trade.get("symbol"),

            "direction":
                trade.get("direction"),

            "entry":
                trade.get("entry"),

            "exit":
                trade.get("exit"),

            "loss":
                trade.get("pnl"),

            "reasons":[]

        }



        # Анализ направления

        if trade.get("direction") == "LONG":

            if trade.get("exit") < trade.get("entry"):

                analysis["reasons"].append(
                    "LONG против движения цены"
                )


        if trade.get("direction") == "SHORT":

            if trade.get("exit") > trade.get("entry"):

                analysis["reasons"].append(
                    "SHORT против движения цены"
                )



        # Анализ уверенности AI

        confidence = trade.get(
            "confidence",
            0
        )


        if confidence < 60:

            analysis["reasons"].append(
                "Сделка открыта при слабом сигнале"
            )



        # Анализ рынка

        regime = trade.get(
            "market_regime"
        )


        if regime == "SIDEWAYS":

            analysis["reasons"].append(
                "Вход во флэтовом рынке"
            )


        if regime == "HIGH_VOLATILITY":

            analysis["reasons"].append(
                "Высокая волатильность"
            )



        self.errors.append(
            analysis
        )


        return analysis



    def get_statistics(self):

        result = {}


        for error in self.errors:

            for reason in error["reasons"]:

                if reason not in result:

                    result[reason] = 0


                result[reason] += 1



        return result



    def report(self):

        return self.errors