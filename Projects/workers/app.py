# from tasks import hello_world

# hello_world.delay()

# docker run -d -p 5672:5672 rabbitmq
# pip install gevent
# celery -A tasks worker -l info -P gevent 
# flower -A tasks
# celery flower --port=5566
# celery -A tasks flower  --address=127.0.0.6 --port=5566

from dataclasses import dataclass
from tasks import ocr_documento

@dataclass
class Pessoa:
    nome: str
    telefone: str
    documento: str 

def cadastro(person: Pessoa):
    ocr_documento.delay(person.documento)

    

person = Pessoa('Eduardo', '1111-2356', 'images\documento_certo.png') 

cadastro(person)


