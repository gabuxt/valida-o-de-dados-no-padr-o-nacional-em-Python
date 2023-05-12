from acesso_cep import BuscaEnderaco
import requests
cep = '02805020'

objeto_cep = BuscaEnderaco(cep)

#r = requests.get(f'https://viacep.com.br/ws/{objeto_cep}/json/')
#print(r.json())

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)