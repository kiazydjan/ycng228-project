

def create_prediction_input(df):
    x_predict = df['close'].fillna(method='bfill').reset_index().drop(columns='index').diff().dropna().T

    return x_predict
