from validate_docbr import CPF, CNPJ

#EXEMPLO DE FACTORY DESIGN PATTERN
class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("A quantidade de dígitos é incorreta!")



class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido")
    
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)



class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido")

    def __str__(self):
        return self.format()
            
    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)



"""Usar para desafio freecodecamp
def format_cpf(self):
    fatia_1 = self.cpf[ :3]
    fatia_2 = self.cpf[3:6]
    fatia_3 = self.cpf[6:9]
    fatia_4 = self.cpf[9: ]
    return(
        "{}.{}.{}-{}".format(fatia_1, fatia_2, fatia_3, fatia_4)
    )
"""