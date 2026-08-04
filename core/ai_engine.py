from ai_model.features import FeatureBuilder
from ai_model.predictor import AIPredictor
from ai_model.decision_engine import DecisionEngine
from ai_model.risk_ai import AIRiskManager
from ai_model.market_regime import MarketRegimeDetector



class AIEngine:


    def __init__(
        self,
        mode="BALANCED"
    ):


        self.mode = mode


        self.feature_builder = FeatureBuilder()


        self.predictor = AIPredictor(
            "ai_model/models/xgboost_v1.pkl"
        )


        self.regime_detector = MarketRegimeDetector()


        self.risk_manager = AIRiskManager(
            mode=mode
        )


        self.decision_engine = DecisionEngine()



    def analyze_market(
        self,
        data
    ):

        return self.regime_detector.detect(
            data
        )



    def prepare_features(
        self,
        data
    ):

        return self.feature_builder.create_features(
            data
        )



    def predict(
        self,
        data
    ):


        features = self.prepare_features(
            data
        )


        latest = features.iloc[-1]


        prediction = self.predictor.predict(
            latest
        )


        return prediction



    def make_decision(
        self,
        signal,
        confidence,
        market_regime,
        data=None
    ):


        ai_prediction = None


        if data is not None:

            ai_prediction = self.predict(
                data
            )



        final_signal = signal

        final_confidence = confidence



        if ai_prediction:


            if ai_prediction["confidence"] >= confidence:

                final_signal = ai_prediction["signal"]

                final_confidence = ai_prediction["confidence"]




        risk = self.risk_manager.analyze(

            confidence=final_confidence,

            market_regime=market_regime["regime"]

        )



        decision = self.decision_engine.decide(

            signal=final_signal,

            confidence=final_confidence,

            risk=risk,

            market_regime=market_regime,

            ai_prediction=ai_prediction

        )



        return {


            "decision": decision,

            "risk": risk,

            "ai_prediction": ai_prediction,

            "market_regime": market_regime,

            "final_signal": final_signal,

            "confidence": final_confidence

        }