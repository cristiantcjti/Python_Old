from celery import Celery
from base64 import standard_b64encode
from httpx import post

app_celery = Celery(
    broker='pyamqp://guest@localhost//'
)


@app_celery.task
def hello_world():
    return 'Hello World'

@app_celery.task
def ocr_documento(documento):
    documento = open(documento, 'rb').read()

    image = standard_b64encode(documento).decode('utf-8')

    data = {
        'image': image
        }

    response = post(
        'https://live-159-external.herokuapp.com/document-to-text',
        json=data,
        timeout=None
        )
    if response.status_code == 200:
        return (response.json())
    raise Exception('An error ocurred.')
