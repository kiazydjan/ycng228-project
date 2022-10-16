from yahoo_fin import stock_info as si


def validate_ticker(ticker):
    valid_tickers = si.tickers_sp500(False)
    if ticker in valid_tickers:
        return True
    else:
        return False


def get_ticker_data(ticker=None, start_date=None, end_date=None):
    if ticker is None:
        return f'No ticker provided to get_ticker_data function'
    else:
        df = si.get_data(ticker, start_date, end_date, index_as_date=False)
        return df
