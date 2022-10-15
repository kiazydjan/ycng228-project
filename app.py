from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return f'Hello dear students, This is a docker test! You should use a better route:!\nEX: get_stock_val/<ticker>\n'

if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=8080, debug=True)