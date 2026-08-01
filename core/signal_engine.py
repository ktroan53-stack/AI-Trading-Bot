def analyze_signal(
    ema_fast,
    ema_slow,
    rsi,
    macd,
    macd_signal,
    price,
    upper_band,
    lower_band,
    atr
):
    """
    Главный движок анализа рынка

    Возвращает:
    BUY
    SELL
    HOLD
    и уровень уверенности
    """

    score = 0
    reasons = []


    # Анализ тренда EMA
    if ema_fast > ema_slow:
        score += 2
        reasons.append(
            "EMA: восходящий тренд"
        )

    elif ema_fast < ema_slow:
        score -= 2
        reasons.append(
            "EMA: нисходящий тренд"
        )


    # RSI
    if rsi < 30:
        score += 1
        reasons.append(
            "RSI: перепроданность"
        )

    elif rsi > 70:
        score -= 1
        reasons.append(
            "RSI: перекупленность"
        )


    # MACD
    if macd > macd_signal:
        score += 2
        reasons.append(
            "MACD: бычий импульс"
        )

    else:
        score -= 2
        reasons.append(
            "MACD: медвежий импульс"
        )


    # Bollinger Bands
    if price < lower_band:
        score += 1
        reasons.append(
            "Цена ниже нижней полосы"
        )

    elif price > upper_band:
        score -= 1
        reasons.append(
            "Цена выше верхней полосы"
        )


    # ATR
    if atr > 0:
        reasons.append(
            "ATR: волатильность учтена"
        )


    # Финальное решение

    if score >= 3:
        signal = "BUY"

    elif score <= -3:
        signal = "SELL"

    else:
        signal = "HOLD"


    confidence = min(
        abs(score) * 15,
        100
    )


    return {
        "signal": signal,
        "score": score,
        "confidence": confidence,
        "reasons": reasons
    }