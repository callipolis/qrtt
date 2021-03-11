# Rate of Change (RoC)

def roc(ohlcv, period=1, ohlcv_series="close"):
    indicator_col = ohlcv[ohlcv_series].pct_change(period)
    return indicator_col
