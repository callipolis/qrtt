# Bollinger Bands (BB)

"""
There are three bands when using Bollinger Bands

Middle Band – 20 Day Simple Moving Average
Upper Band – 20 Day Simple Moving Average + (Standard Deviation x 2)
Lower Band – 20 Day Simple Moving Average - (Standard Deviation x 2)
"""


def bbands(ohlcv, period=20, number_of_std=2, ohlcv_series="close"):
    """
    Outcomes have been validated using data from Bloomberg and TradingView.
    """
    _ohlcv = ohlcv[[ohlcv_series]].copy(deep=True)
    _ohlcv["mid_band"] = _ohlcv[ohlcv_series].rolling(window=period, min_periods=period).mean()

    _ohlcv["std"] = _ohlcv[ohlcv_series].rolling(window=period, min_periods=period).std(ddof=0)
    _ohlcv["lower_band"] = _ohlcv["mid_band"] - number_of_std * _ohlcv["std"]
    _ohlcv["upper_band"] = _ohlcv["mid_band"] + number_of_std * _ohlcv["std"]

    return _ohlcv[["lower_band", "mid_band", "upper_band"]]

#
def pct_bbands(ohlcv, period=20, number_of_std=2, ohlcv_series="close"):
    """
    Outcomes have been validated using data from Bloomberg and TradingView.
    """
    _ohlcv = ohlcv[[ohlcv_series]].copy(deep=True)
    _ohlcv["mid_band"] = _ohlcv[ohlcv_series].rolling(window=period, min_periods=period).mean()

    _ohlcv["std"] = _ohlcv[ohlcv_series].rolling(window=period, min_periods=period).std(ddof=0)
    _ohlcv["lower_band"] = _ohlcv["mid_band"] - number_of_std * _ohlcv["std"]
    _ohlcv["upper_band"] = _ohlcv["mid_band"] + number_of_std * _ohlcv["std"]

    indicator_values = (_ohlcv[ohlcv_series] - _ohlcv['lower_band']) / (_ohlcv['upper_band'] - _ohlcv['lower_band'])

    return indicator_values

