import requests

class BuscaEnderaco:
    def __init__(self, cep):
        teste = str(cep)
        if self.cep_e_valido(teste):
            self.cep = teste
        else:
            raise ValueError("CEP invalido")

    def __str__(self):
        return self.format()

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acessa_via_cep(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        dados = r.json()
        return {
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        }













