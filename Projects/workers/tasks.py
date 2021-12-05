from celery import Celery
from celery.contrib import rdb 
from base64 import standard_b64encode
from httpx import post, get

app_celery = Celery(
    broker='pyamqp://guest@localhost//'
)


@app_celery.task
def hello_world():
    return 'Hello World'

@app_celery.task(
    name="Taks' name",
    bind=True,
    #default_retry_delay=3,
    #max_retry=5,
    #or
    retry_backoff=True, # 2s,4s,8s,16s,32s..
    #backoff=3 # 3s,6s,12s,24s
    autoretry_for=(ValueError,),
    )
def ocr_document(self,documento):
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
        #check_cpf.delay(response.json()['cpf']) #encadeia task
        return response.json()
    
    # self.retry()
    raise ValueError('An error ocurred.')


class CPFError(BaseException):
    ...

@app_celery.task(
    bind=True,
    default_retry_delay=20,
    autoretry_for=(CPFError,)
)
def check_cpf(self, cpf):
    if isinstance(cpf, dict):
        cpf = cpf['cpf']

    response = get(
        f'https://live-159-external.herokuapp.com/check-cpf?cpf={cpf}',
        timeout=None
    )
    #rdb.set_trace() #to debug

    if response.status_code == 200:
        return response.json()['cpf-status']
    raise CPFError('CPF is not valid')
