from acesso_cep import BuscaEndereco


cep = '01001000'

objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)



"""

#DATAS

cadastro = DatasBr()

print(cadastro.tempo_cadastro())
#*********************




#FORMATACAO TELEFONE
#from telefonesBr import TelefonesBr
#import re

telefone = "552126481234"

telefone_objetos = TelefonesBr(telefone)

print(telefone_objetos)
#*********************


# CPF / CNPJ
#from cpf_cnpj import Documento
#from validate_docbr import CNPJ

#TESTE DE CPF
cpf = "15316264754"
doc_cpf = Documento.cria_documento(cpf)
print(doc_cpf)

#TESTE DE CNPJ
cnpj = "35379838000112"
doc_cnpj = Documento.cria_documento(cnpj)
print(doc_cnpj)
#*********************
"""