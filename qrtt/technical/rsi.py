## Regular RSI

def rsi(ohlcv, period=14, ohlcv_series="close", average_method="traditional", indicator_name="rsi"):
    _ohlcv = ohlcv.copy(deep=True)
    _ohlcv["diff"] = _ohlcv[ohlcv_series].diff(periods=1)
    _ohlcv["diff_up"] = _ohlcv["diff"][_ohlcv["diff"] >= 0]
    _ohlcv["diff_down"] = _ohlcv["diff"][_ohlcv["diff"] < 0]

    _ohlcv["diff_up"].fillna(value=0, inplace=True)
    _ohlcv["diff_down"].fillna(value=0, inplace=True)

    if average_method == "traditional":
        _ohlcv["rsi_u"] = _ohlcv["diff_up"].rolling(window=period, min_periods=period).mean()
        _ohlcv["rsi_d"] = _ohlcv["diff_down"].rolling(window=period, min_periods=period).mean()

        for i in range(period, _ohlcv.shape[0]):
            _ohlcv.iloc[i, _ohlcv.columns.get_loc("rsi_u")] = (_ohlcv.iloc[i - 1, _ohlcv.columns.get_loc("rsi_u")] * (
                    period - 1) + _ohlcv.iloc[i, _ohlcv.columns.get_loc("diff_up")]) / period
            _ohlcv.iloc[i, _ohlcv.columns.get_loc("rsi_d")] = (_ohlcv.iloc[i - 1, _ohlcv.columns.get_loc("rsi_d")] * (
                    period - 1) + _ohlcv.iloc[i, _ohlcv.columns.get_loc("diff_down")]) / period
            # _ohlcv["rsi_u"][i] = (_ohlcv["rsi_u"][i - 1] * (period - 1) + _ohlcv["diff_up"][i]) / period
            # _ohlcv["rsi_d"][i] = (_ohlcv["rsi_d"][i - 1] * (period - 1) + _ohlcv["diff_down"][i]) / period

    elif average_method == "sma":
        _ohlcv["rsi_u"] = _ohlcv["diff_up"].rolling(window=period, min_periods=period).mean()
        _ohlcv["rsi_d"] = _ohlcv["diff_down"].rolling(window=period, min_periods=period).mean()
    elif average_method == "ema":
        _ohlcv["rsi_u"] = _ohlcv["diff_up"].ewm(span=period, min_periods=period).mean()
        _ohlcv["rsi_d"] = _ohlcv["diff_down"].ewm(span=period, min_periods=period).mean()

    # These codes are needed if sma calculation method is changed to count only days with data (N excludes days without data)
    # data_rsi["rsi_u"].iloc[periods:data_rsi.shape[0]].fillna(value=0, inplace = True)
    # data_rsi["rsi_d"].iloc[periods:data_rsi.shape[0]].fillna(value=0, inplace = True)

    # ohlc.dropna(inplace=dropna)  # Drop NA if set to True

    _ohlcv["rs"] = abs(_ohlcv["rsi_u"]) / abs(_ohlcv["rsi_d"])
    _ohlcv[indicator_name] = 100 - (100 / (1 + _ohlcv["rs"]))

    # ohlc.drop(columns=['diff', 'diff_up', 'diff_down', 'rsi_u', 'rsi_d', 'rs'], inplace=True)

    # data_rsi[indicator_name].iloc[0:periods] = np.nan
    return _ohlcv[indicator_name]
