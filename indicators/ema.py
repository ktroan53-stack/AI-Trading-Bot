def calculate_ema(data, period=20):
    return data["close"].ewm(span=period, adjust=False).mean()