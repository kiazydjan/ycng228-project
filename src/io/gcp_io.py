import logging

import joblib
from google.api_core.exceptions import NotFound
from google.cloud import storage


def get_model_from_bucket(model_filename, bucket_name):
    log = logging.getLogger()
    client = storage.Client()
    b = client.get_bucket(bucket_name)
    blob = storage.Blob(f'{model_filename}', b)
    try:
        with open(f'{model_filename}', 'wb') as file_obj:  # critical resource should use tempfile...

            client.download_blob_to_file(blob, file_obj)
        with open(f'{model_filename}', 'rb') as file_obj:
            model = joblib.load(file_obj)
    except NotFound as e:
        log.warning(f'model {model_filename} not found\n')
        model = None

    return model
