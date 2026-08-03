from ai_model.ensemble import AIEnsemble
from ai_model.decision_engine import DecisionEngine
from ai_model.risk_ai import AIRiskManager
from ai_model.market_regime import MarketRegimeDetector


class AIEngine:
    """
    Главный AI управляющий модуль

    Объединяет:
    - AI модели
    - анализ рынка
    - риск менеджмент
    - принятие решения
    """

    def __init__(
        self,
        mode="BALANCED"
    ):

        self.ensemble = AIEnsemble()

        self.regime_detector = MarketRegimeDetector()

        self.decision_engine = DecisionEngine()

        self.risk_manager = AIRiskManager(
            mode=mode
        )


    def analyze_market(
        self,
        df
    ):

        # 1. Определяем состояние рынка

        regime = self.regime_detector.detect(
            df
        )


        return regime



    def make_decision(
        self,
        signal,
        confidence,
        market_regime,
        drawdown=0
    ):


        # 2. Проверяем риск

        risk = self.risk_manager.analyze(

            confidence,

            market_regime,

            drawdown

        )


        # 3. Финальное решение

        decision = self.decision_engine.analyze(

            ai_signal=signal,

            confidence=confidence,

            market_regime=market_regime,

            risk_allowed=risk["allowed"]

        )


        return {

            "decision":
                decision,

            "risk":
                risk

        }