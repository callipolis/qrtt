# MACD

def MACD(ohlc, short_period=12, long_period=26, signal_period=9, ohlcv_series="close", average_method="ema",
         dropna=True):
    if average_method == "ema":
        ohlc["short"] = ohlc[ohlcv_series].ewm(span=short_period, min_periods=short_period).mean()
        ohlc["long"] = ohlc[ohlcv_series].ewm(span=long_period, min_periods=long_period).mean()
    elif average_method == "sma":
        ohlc["short"] = ohlc[ohlcv_series].rolling(window=short_period, min_periods=short_period).mean()
        ohlc["long"] = ohlc[ohlcv_series].rolling(window=long_period, min_periods=long_period).mean()

    ohlc["macd"] = ohlc["short"] - ohlc["long"]

    if average_method == "ema":
        ohlc["signal"] = ohlc["macd"].ewm(span=signal_period, min_periods=signal_period).mean()
    elif average_method == "sma":
        ohlc["signal"] = ohlc["macd"].rolling(window=signal_period, min_periods=signal_period).mean()

    ohlc["hist"] = ohlc["macd"] - ohlc["signal"]

    ohlc.drop(columns=['short', 'long'], inplace=True)

    ohlc.dropna(inplace=dropna)  # Drop NA if set to True

    return ohlc
