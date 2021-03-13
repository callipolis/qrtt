import numpy as np



def wma(ohlcv, period=10, ohlcv_series="close"):
    """
    Return the weighted moving average (WMA) values
    """
    _ohlcv = ohlcv[[ohlcv_series]].copy(deep=True).sort_index(ascending=True)
    weights = np.arange(1, period+1)
    indicator_values = _ohlcv[ohlcv_series].rolling(window=period, min_periods=period).\
        apply(lambda x: np.dot(x, weights)/weights.sum(), raw=True)

    return indicator_values
