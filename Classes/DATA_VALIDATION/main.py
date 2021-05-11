
from cpf_cnpj import Documento
from validate_docbr import CNPJ

#cpf = Cpf(23034704801)

#cpf = CPF()

#object_cpf = Cpf(cpf)

#print(object_cpf)

#print(cpf)

#print(doc_cnpj.validate((cnpj)))

cpf = "15316264754"
doc_cpf = Documento.cria_documento(cpf)
print(doc_cpf)



cnpj = "35379838000112"
doc_cnpj = Documento.cria_documento(cnpj)
print(doc_cnpj)







