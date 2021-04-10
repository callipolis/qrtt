"""
From Bloomberg:

    Stochastics measures the velocity of a security's price movement to identify 
    overbought and oversold conditions. The indicator measures current price relative 
    to highs and lows over a time period. In an up-trend, markets tend to close near 
    the high and  while in a down-trend they to close nearer to the lows. 

    This indicator is calculated with the following formula:

    %K = 100*Closing Range/Total Range

    where:

    Closing Range = Close - Range Minimum
    Total Range = Range Maximum - Range Minimum

    The extent of the Range is determined by the %K period parameter.

    %D = N-period moving average of %K where N is the %D period parameter.

    %K with %D is sometimes referred to as the Fast Stochastics. 
    %DS and %DSS, sometimes referred to as the Slow Stochastics, 
    have additional smoothing as determined by their respective period parameters. 

    Stochastics can be used to recognize potential turning points to help make entry/exit decisions.

From StockCharts.com

    Developed by George C. Lane in the late 1950s, the Stochastic Oscillator is a momentum indicator 
    that shows the location of the close relative to the high-low range over a set number of periods. 
    According to an interview with Lane, the Stochastic Oscillator “doesn't follow price, it doesn't 
    follow volume or anything like that. It follows the speed or the momentum of price. As a rule, 
    the momentum changes direction before price.” As such, bullish and bearish divergences in the 
    Stochastic Oscillator can be used to foreshadow reversals. This was the first, and most important, 
    signal that Lane identified. Lane also used this oscillator to identify bull and bear set-ups to 
    anticipate a future reversal. As the Stochastic Oscillator is range-bound, it is also useful for 
    identifying overbought and oversold levels.

"""

import pandas as pd

def stoch_k(ohlcv, k_period=20):
    """[summary]

    Args:
        ohlcv ([type]): [description]
        k_period (int, optional): [description]. Defaults to 20.

    Returns:
        [type]: [description]
    """
    _ohlcv = ohlcv[['high', 'low', 'close']].copy(deep=True)
    _ohlcv['period_low'] = _ohlcv['low'].rolling(window=k_period).min()
    _ohlcv['period_high'] = _ohlcv['high'].rolling(window=k_period).max()
    indicator_values = 100 * (_ohlcv['close'] - _ohlcv['period_low']) / (
        _ohlcv['period_high'] - _ohlcv['period_low'])
    return indicator_values


def stoch_d(ohlcv, k_period=20, d_period=5):
    _k_values = stoch_k(ohlcv, k_period=k_period)
    indicator_values = _k_values.rolling(window=d_period).mean()
    return indicator_values


def stoch_ds(ohlcv, k_period=20, d_period=5, ds_period=5):
    _d_values = stoch_d(ohlcv, k_period=k_period, d_period=d_period)
    indicator_values = _d_values.rolling(window=ds_period).mean()
    return indicator_values


def stoch_dss(ohlcv, k_period=20, d_period=5, ds_period=5, dss_period=3):
    _ds_values = stoch_ds(ohlcv, k_period, d_period, ds_period)
    indicator_values = _ds_values.rolling(window=dss_period).mean()
    return indicator_values


def stoch_fast(ohlcv, k_period=20, d_period=5):
    _k_values = stoch_k(ohlcv, k_period)
    _d_values = stoch_d(ohlcv, k_period, d_period)
    _stoch_df = pd.concat([_k_values, _d_values], axis=1, keys=['%k', '%d'])
    return _stoch_df


def stoch_slow(ohlcv, k_period=20, d_period=5, dd_period=5):
    _d_values = stoch_d(ohlcv, k_period, d_period)
    _ds_values = stoch_ds(ohlcv, k_period, d_period, dd_period)
    _stoch_df = pd.concat([_d_values, _ds_values], axis=1, keys=['%d', '%ds'])
    return _stoch_df


def stoch_full(ohlcv, k_period=20, d_period=5, dd_period=5, dss_period=3):
    _ds_values = stoch_ds(ohlcv, k_period, d_period, dd_period)
    _dss_values = stoch_dss(ohlcv, k_period, d_period, dd_period, dss_period)
    _stoch_df = pd.concat([_ds_values, _dss_values],
                          axis=1,
                          keys=['%ds', '%dss'])
    return _stoch_df


def stoch_complete(ohlcv, k_period=20, d_period=5, dd_period=5, dss_period=3):
    _k_values = stoch_k(ohlcv, k_period)
    _d_values = stoch_d(ohlcv, k_period, d_period)
    _ds_values = stoch_ds(ohlcv, k_period, d_period, dd_period)
    _dss_values = stoch_dss(ohlcv, k_period, d_period, dd_period, dss_period)
    _stoch_df = pd.concat([_k_values, _d_values, _ds_values, _dss_values],
                          axis=1,
                          keys=['%k', '%d', '%ds', '%dss'])
    return _stoch_df
