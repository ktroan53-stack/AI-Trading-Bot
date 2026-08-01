from data.market_data import load_candles
from core.signal_engine import analyze_signal


def main():

    print("=" * 45)
    print("        AI TRADING BOT v0.2")
    print("=" * 45)


    data = load_candles()

    last = data.iloc[-1]


    print()
    print("BTCUSDT")
    print("-" * 45)


    print(f"Цена: {last['close']:.2f}")
    print(f"EMA20: {last['EMA20']:.2f}")
    print(f"EMA50: {last['EMA50']:.2f}")
    print(f"RSI14: {last['RSI14']:.2f}")
    print(f"ADX: {last['ADX']:.2f}")



    print()


    if last["EMA20"] > last["EMA50"]:

        print("Тренд: ВОСХОДЯЩИЙ")

    else:

        print("Тренд: НИСХОДЯЩИЙ")



    print()


    if last["RSI14"] > 70:

        print("RSI: Перекупленность")

    elif last["RSI14"] < 30:

        print("RSI: Перепроданность")

    else:

        print("RSI: Нейтральная зона")



    print()

    print("-" * 45)
    print("AI ANALYSIS")
    print("-" * 45)



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

    print(
        f"Сигнал: {result['signal']}"
    )


    print(
        f"Уверенность: {result['confidence']}%"
    )


    print(
        f"Score: {result['score']}"
    )


    print()

    print("Причины:")


    for reason in result["reasons"]:

        print(
            "-",
            reason
        )



    print("=" * 45)



if __name__ == "__main__":

    main()