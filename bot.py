from data.market_data import load_candles


def main():
    print("=" * 45)
    print("        AI TRADING BOT v0.1")
    print("=" * 45)

    data = load_candles()

    last = data.iloc[-1]

    print()
    print("BTCUSDT")
    print("-" * 45)

    print(f"Цена:   {last['close']:.2f}")
    print(f"EMA20:  {last['EMA20']:.2f}")
    print(f"RSI14:  {last['RSI14']:.2f}")

    print()

    if last["close"] > last["EMA20"]:
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

    if last["close"] > last["EMA20"] and last["RSI14"] < 70:
        print("Рекомендация: LONG")

    elif last["close"] < last["EMA20"] and last["RSI14"] > 30:
        print("Рекомендация: SHORT")

    else:
        print("Рекомендация: WAIT")

    print("=" * 45)


if __name__ == "__main__":
    main()