def calculate_bollinger_bands(data, period=20, std_dev=2):
    """
    Расчет полос Боллинджера

    period - период средней
    std_dev - количество стандартных отклонений
    """

    middle_band = data["close"].rolling(
        window=period
    ).mean()


    standard_deviation = data["close"].rolling(
        window=period
    ).std()


    upper_band = middle_band + (
        standard_deviation * std_dev
    )


    lower_band = middle_band - (
        standard_deviation * std_dev
    )


    return (
        upper_band,
        middle_band,
        lower_band
    )