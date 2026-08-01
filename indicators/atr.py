def calculate_atr(data, period=14):
    """
    Average True Range (ATR)

    Показывает волатильность рынка
    """

    high_low = data["high"] - data["low"]

    high_close = abs(
        data["high"] - data["close"].shift()
    )

    low_close = abs(
        data["low"] - data["close"].shift()
    )


    true_range = data[
        [
            "high",
            "low",
            "close"
        ]
    ].copy()


    true_range["tr"] = high_low.combine(
        high_close,
        max
    ).combine(
        low_close,
        max
    )


    atr = true_range["tr"].rolling(
        window=period
    ).mean()


    return atr