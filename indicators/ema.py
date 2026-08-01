def calculate_ema(data, period):
    """
    Расчет экспоненциальной скользящей средней (EMA).

    data   - DataFrame с колонкой 'close'
    period - период EMA
    """

    return data["close"].ewm(
        span=period,
        adjust=False
    ).mean()