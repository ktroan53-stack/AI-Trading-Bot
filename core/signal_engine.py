def analyze_signal(
    ema_fast,
    ema_slow,
    rsi,
    macd,
    macd_signal,
    price,
    upper_band,
    lower_band,
    atr,
    adx
):

    score = 0
    reasons = []


    # TREND EMA

    if ema_fast > ema_slow:

        score += 3

        reasons.append(
            "EMA: восходящий тренд"
        )

    else:

        score -= 3

        reasons.append(
            "EMA: нисходящий тренд"
        )



    # ADX - сила тренда

    if adx < 20:

        reasons.append(
            "ADX: слабый тренд"
        )


    elif adx < 40:

        reasons.append(
            "ADX: нормальная сила тренда"
        )


    else:

        reasons.append(
            "ADX: сильный тренд"
        )

        # усиливаем уверенность

        if score > 0:
            score += 1

        elif score < 0:
            score -= 1



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

    else:

        reasons.append(
            "RSI: нормальная зона"
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



    # Bollinger

    if price < lower_band:

        score += 1

        reasons.append(
            "Цена ниже диапазона"
        )


    elif price > upper_band:

        score -= 1

        reasons.append(
            "Цена выше диапазона"
        )


    else:

        reasons.append(
            "Цена внутри диапазона"
        )



    # ATR

    if atr > 0:

        reasons.append(
            "ATR: риск учтен"
        )



    # DECISION

    if score >= 4:

        signal = "BUY"


    elif score <= -4:

        signal = "SELL"


    else:

        signal = "HOLD"



    confidence = min(
        abs(score) * 12,
        100
    )


    return {

        "signal": signal,

        "score": score,

        "confidence": confidence,

        "reasons": reasons
    }