# from tasks import hello_world

# hello_world.delay()


from celery import chain 
from dataclasses import dataclass
from tasks import ocr_document, check_cpf

@dataclass
class Person:
    nome: str
    telefone: str
    documento: str 

def cadastro(person: Person):
#    data = ocr_document.delay(
#        person.documento
#        )

#    check_cpf.delay(data['cpf']) 

    chain_go = chain(
        ocr_document.s(person.documento),
        check_cpf.s()
    )
    
    chain_go()

    return 'Your registration is under analyse.'

person = Person('Eduardo', '1111-2356', 'images\documento_certo.png') 

print(cadastro(person))



