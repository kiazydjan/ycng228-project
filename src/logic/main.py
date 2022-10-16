from src.io.gcp_io import get_model_from_bucket
from src.io.fetch_data import get_ticker_data
from src.model.transform_data import create_prediction_input


class BusinessLogic:

    def __init__(self):
        self._root_bucket = 'ycng228-karen-iazydjan-bucket'
        self._model_name = 'mdl.sav'

    def get_model(self):
        model = get_model_from_bucket(self._model_name, self._root_bucket)

        return model

    def do_predictions_for(self, ticker):
        model = self.get_model()
        prediction = model.predict(create_prediction_input(get_ticker_data(ticker, 30)))

        return prediction

    def give_stock_advice(self, ticker):
        prediction = self.do_predictions_for(ticker)
        if prediction == 1:
            return f'You should buy {ticker} stock \n'
        else:
            return f'You should sell {ticker} stock \n'
