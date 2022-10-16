from yahoo_fin import stock_info as si


def validate_ticker(ticker):
    valid_tickers = si.tickers_sp500(False)
    if ticker in valid_tickers:
        return True
    else:
        return False


def get_ticker_data(ticker=None, lag=None):
    if ticker is None:
        return f'No ticker provided to get_ticker_data function'
    else:
        if lag is None:
            df = si.get_data(ticker, index_as_date=False)
        else:
            df = si.get_data(ticker, index_as_date=False).tail(lag+1)
        return df
