import pandas as pd


def load_daily_stock_data(symbol="SPY"):
    """
    This function returns daily OHLCV data for a specific stock

    RETURN OHLCV data in Pandas Dataframe
    """
    base_url = 'https://data.qrtt.org/equity/us/aggregates/1d/'
    file_name = f'{symbol}.csv'
    file_url = base_url + file_name
    _df = pd.read_csv(file_url, parse_dates=['timestamp'], infer_datetime_format=True, index_col='timestamp')
    return _df


