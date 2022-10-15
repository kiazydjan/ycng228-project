from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return f'Hello dear students, This is a docker test! You should use a better route:!\nEX: get_stock_val/<ticker>\n'