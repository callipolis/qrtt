import pandas as pd

def testfunction1():
    print('Test Function')


def load_stock_data(symbol="SPY"):
    base_url = 'https://data.qrtt.org/equity/us/aggregates/1d/'
    file_name = f'{symbol}.csv'
    file_url = base_url + file_name
    _df = pd.read_csv(file_url, parse_dates=['timestamp'], infer_datetime_format=True, index_col='timestamp')
    return _df
