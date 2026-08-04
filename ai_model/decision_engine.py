class DecisionEngine:
    """
    Decision Fusion Engine v0.2

    Объединяет решения отделов:

    - Technical Signal
    - AI Ensemble
    - Market Regime
    - Risk Department
    """


    def __init__(self):

        self.weights = {

            "technical": 0.4,

            "ai": 0.6

        }



    def decide(
        self,
        signal,
        confidence,
        risk,
        market_regime,
        ai_prediction=None
    ):


        if not risk["allowed"]:

            return {

                "action": "HOLD",

                "reason":
                    risk["reason"],

                "confidence":
                    confidence

            }



        final_score = 0

        explanations = []



        # Technical analysis

        if signal == "BUY":

            final_score += self.weights["technical"]

            explanations.append(
                "Technical BUY"
            )


        elif signal == "SELL":

            final_score -= self.weights["technical"]

            explanations.append(
                "Technical SELL"
            )



        # AI analysis

        if ai_prediction:

            ai_signal = ai_prediction.get(
                "signal"
            )

            ai_confidence = ai_prediction.get(
                "confidence",
                0
            )


            ai_strength = ai_confidence / 100



            if ai_signal == "BUY":

                final_score += (
                    self.weights["ai"]
                    *
                    ai_strength
                )

                explanations.append(
                    "AI BUY"
                )


            elif ai_signal == "SELL":

                final_score -= (
                    self.weights["ai"]
                    *
                    ai_strength
                )

                explanations.append(
                    "AI SELL"
                )



        # Market filter

        if market_regime["regime"] == "SIDEWAYS":

            final_score *= 0.5

            explanations.append(
                "Sideways market filter"
            )



        # Final decision

        if final_score >= 0.5:

            return {

                "action": "BUY",

                "reason": explanations,

                "score": round(
                    final_score,
                    2
                )

            }



        if final_score <= -0.5:

            return {

                "action": "SELL",

                "reason": explanations,

                "score": round(
                    final_score,
                    2
                )

            }



        return {

            "action": "HOLD",

            "reason": explanations,

            "score": round(
                final_score,
                2
            )

        }