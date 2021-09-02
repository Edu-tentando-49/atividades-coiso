from unidade_federativa import Unidade_Federativa

unidadesFederativas = Unidade_Federativa.get_lista_UF()
for uf in unidadesFederativas:
    print(uf)

for sigla in unidadesFederativas:
    sigla = input("aaa")
    estado = Unidade_Federativa.get_uf(sigla)
    print("A sigla de " + sigla + " é o estado de " + estado)