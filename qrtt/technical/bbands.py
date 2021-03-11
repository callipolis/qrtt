
# Bollinger Bands (BB)

"""
There are three bands when using Bollinger Bands

Middle Band – 20 Day Simple Moving Average
Upper Band – 20 Day Simple Moving Average + (Standard Deviation x 2)
Lower Band – 20 Day Simple Moving Average - (Standard Deviation x 2)
"""


def BollingerBand(input_dataset, std_periods=20, number_of_std=2, ohlcv_series="close", average_method="sma"):
    # Add Columns to DataFrame Specifically Needed for Bollinger Band Indicator
    input_dataset["std"] = input_dataset[ohlcv_series].rolling(window=std_periods).std()
    # input_dataset["std"] = input_dataset[ohlcv_series].shift(1).rolling(window=std_periods).std()
    # Need to see if we need to shift one row down to avoid look ahead bias

    input_dataset["mid_band"] = input_dataset["close"].rolling(window=std_periods).mean()
    # input_dataset["mid_band"] = input_dataset["close"].shift(1).rolling(window=std_periods).mean()

    input_dataset["lower_band"] = input_dataset["mid_band"] - number_of_std * input_dataset["std"]
    input_dataset["upper_band"] = input_dataset["mid_band"] + number_of_std * input_dataset["std"]

    # data["band_size"] = data["upper_band"] - data["lower_band"]
    # data["avg_band_size"] = data["band_size"].expanding().mean()
    # data["vol_sma"] = data["volume"].rolling(window=30).mean()
    # data["vol_diff"] = data["volume"] - data["vol_sma"] * 1.5
    # data["rsi"] = technical_indicators.RSI(data = data, periods = 14)
    # data["sma2"] = technical_indicators.SMA_2L(data = data, short = 5, long = 30)
    # data["MACD"] = technical_indicators.MACD(data = data)
    # data["ROC"] = technical_indicators.RateofChange(data)

    return input_dataset


def add_percentB(ohlcv_dataset, ohlc_series="close", time_periods=[14, 30], average_method="sma", number_of_std=2):
    # Add Columns to DataFrame Specifically Needed for Bollinger Band Indicator

    indicators_list = []

    for period in time_periods:
        indicator_name = f"percentB_{ohlc_series[0]}_{period}"

        data_series = pd.DataFrame(ohlcv_dataset[ohlc_series])

        data_series["std"] = data_series[ohlc_series].rolling(window=period).std()
        data_series["mid_band"] = data_series["close"].rolling(window=period).mean()
        data_series["lower_band"] = data_series["mid_band"] - number_of_std * data_series["std"]
        data_series["upper_band"] = data_series["mid_band"] + number_of_std * data_series["std"]

        ohlcv_dataset[indicator_name] = (data_series[ohlc_series] - data_series["lower_band"]) / (
                    data_series["upper_band"] - data_series["lower_band"])

        indicators_list.append(indicator_name)

    return ohlcv_dataset, indicators_list


### Customized BB Indicator


def add_stdB_indicators(ohlcv_dataset, ohlc_series="close", time_periods=[14, 30], average_method="sma"):
    # Add Columns to DataFrame Specifically Needed for Bollinger Band Indicator

    indicators_list = []

    for period in time_periods:
        indicator_name = f"stdB_{ohlc_series[0]}_{period}"

        data_series = pd.DataFrame(ohlcv_dataset[ohlc_series])

        data_series["std"] = data_series[ohlc_series].rolling(window=period).std()
        data_series["mid_band"] = data_series["close"].rolling(window=period).mean()

        ohlcv_dataset[indicator_name] = (data_series[ohlc_series] - data_series["mid_band"]) / data_series["std"]

        indicators_list.append(indicator_name)

    return ohlcv_dataset, indicators_list
