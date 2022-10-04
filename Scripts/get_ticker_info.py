from yahoo_fin import stock_info as si

ticker_info = si.tickers_sp500(True)
ticker_info.to_csv("_SP500_ticker_info.csv" , index=False , encoding='utf-8-sig')
