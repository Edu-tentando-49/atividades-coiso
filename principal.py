from unidade_federativa import Unidade_Federativa

unidadesFederativas = Unidade_Federativa.get_lista_UF()


for sigla in unidadesFederativas:
    print(sigla)

sigla = input("digite a sigla do estado que procura ")
estado = Unidade_Federativa.get_uf(sigla)
print('O estado de ' + sigla + ' é ' + estado)
