
# Expotential Moving Average (EMA)

def ema(ohlcv, period=10, ohlcv_series="close"):
    indicator_col = ohlcv[ohlcv_series].ewm(span=period, min_periods=period).mean()
    return indicator_col
