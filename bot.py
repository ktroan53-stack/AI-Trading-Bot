from data.market_data import load_candles
from core.signal_engine import analyze_signal
from core.ai_engine import AIEngine



def main():

    print("=" * 55)
    print("        AI TRADING BOT v0.3")
    print("        AI ENGINE INTEGRATION")
    print("=" * 55)


    ai = AIEngine(
        mode="BALANCED"
    )


    data = load_candles()

    last = data.iloc[-1]


    print()

    print("BTCUSDT")
    print("-" * 55)


    print(f"Цена: {last['close']:.2f}")
    print(f"EMA20: {last['EMA20']:.2f}")
    print(f"EMA50: {last['EMA50']:.2f}")
    print(f"RSI14: {last['RSI14']:.2f}")
    print(f"ADX: {last['ADX']:.2f}")


    result = analyze_signal(

        ema_fast=last["EMA20"],

        ema_slow=last["EMA50"],

        rsi=last["RSI14"],

        macd=last["MACD"],

        macd_signal=last["MACD_SIGNAL"],

        price=last["close"],

        upper_band=last["BB_UPPER"],

        lower_band=last["BB_LOWER"],

        atr=last["ATR"],

        adx=last["ADX"]

    )


    print()

    print("-" * 55)

    print("TECHNICAL ANALYSIS")

    print("-" * 55)


    print(
        f"Сигнал: {result['signal']}"
    )

    print(
        f"Уверенность: {result['confidence']}%"
    )

    print(
        f"Score: {result['score']}"
    )


    market_regime = ai.analyze_market(
        data
    )


    final = ai.make_decision(

        signal=result["signal"],

        confidence=result["confidence"],

        market_regime=market_regime,

        data=data

    )


    print()

    print("-" * 55)

    print("AI ENGINE")

    print("-" * 55)


    print(
        f"Режим рынка: {market_regime}"
    )


    print()

    print("AI Prediction:")

    print(
        final["ai_prediction"]
    )


    print()

    print("FINAL DECISION")

    print("-" * 55)


    print(
        f"Решение: {final['decision']}"
    )


    print(
        f"Риск: {final['risk']}"
    )


    print("=" * 55)



if __name__ == "__main__":

    main()