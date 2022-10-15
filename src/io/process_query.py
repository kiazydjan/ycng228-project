# from datetime import datetime, timedelta

from yahoo_fin import stock_info as si


def validate_ticker(ticker):
    valid_tickers = si.tickers_sp500(False)
    if ticker in valid_tickers:
        return True
    else:
        return False
