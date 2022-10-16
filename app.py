from flask import Flask
from src.io.fetch_data import validate_ticker

app = Flask(__name__)


@app.route('/', methods=['GET'])
def no_ticker_provided():
    return f'Please provide a valid SP500 ticker: \nEX: [...]/stock_advice/<ticker>\n'


@app.route('/stock_advice/<ticker>', methods=['GET'])
def fetch_stock_strategy(ticker):
    if validate_ticker(ticker):
        strategy = 'You provided a valid ticker'
        return f'{strategy}\n'
    else:
        return f'{ticker} is not an a valid SP500 ticker. Please provide a valid SP500 ticker.\n'


if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=8080, debug=True)
