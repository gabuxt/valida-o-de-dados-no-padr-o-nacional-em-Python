from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if (len(documento) == 11):
            return DocCpf(documento)
        elif (len(documento) == 14):
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos invalida")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def format(self):
         mascara = CPF()
         return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cpnj inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def format(self):
         mascara = CNPJ()
         return mascara.mask(self.cnpj)














