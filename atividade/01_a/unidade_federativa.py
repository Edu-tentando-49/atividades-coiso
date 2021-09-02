class Unidade_Federativa:
    @staticmethod
    def get_lista_UF():
        vetor_uf = [
            "Santa Catarina / SC",
            "Rio Grande do Sul / RS",
            "Acre / AC",
            "Alagoas / AL",
            "Amazonas / AM",
            "Bahia / BA",
            "Amapá / AP",
            "Ceará / CE",
            "Distrito Federal / DF",
            "Espírito Santo / ES",
            "Goiás / GO",
            "Maranhão / MA",
            "Mato Grosso / MT",
            "Mato Grosso do Sul / MS",
            "Minas Gerais / MG",
            "Pará / PA",
            "Paraíba / PB",
            "Paraná / PR",
            "Pernambuco / PE",
            "Piauí / PI",
            "Rio de Janeiro / RJ",
            "Rio Grande do Norte / RN",
            "Rondônia / RO",
            "Roraima / RR",
            "São Paulo / SP",
            "Sergipe / SE",
            "Tocantins / TO"]
        return vetor_uf


    @staticmethod
    def get_uf(sigla):
        if (sigla == 'SC'):
            return 'Santa Catarina'
        elif (sigla == 'RS'):
            return 'Rio Grande do sul'
        elif (sigla == 'AC'):
            return 'Acre'
        elif (sigla == 'AL'):
            return 'Alagoas'
        elif (sigla == 'AM'):
            return 'Amazonas'
        elif (sigla == 'BA'):
            return 'Bahia'
        elif (sigla == 'AP'):
            return 'Amapá'
        elif (sigla == 'CE'):
            return 'Ceará'
        elif (sigla == 'DF'):
            return 'Distrito Federal'
        elif (sigla == 'ES'):
            return 'Espírito Santo'
        elif (sigla == 'GO'):
            return 'Goiás'
        elif (sigla == 'MA'):
            return 'Maranhão'
        elif (sigla == 'MT'):
            return 'Mato Grosso'
        elif (sigla == 'MS'):
            return 'Mato Grosso do Sul'
        elif (sigla == 'MG'):
            return 'Minas Gerais'
        elif (sigla == 'PA'):
            return 'Pará'
        elif (sigla == 'PB'):
            return 'Paraíba'
        elif (sigla == 'PR'):
            return 'Paraná'
        elif (sigla == 'PE'):
            return 'Pernambuco'
        elif (sigla == 'PI'):
            return 'Piauí'
        elif (sigla == 'RJ'):
            return 'Rio de Janeiro'
        elif (sigla == 'RN'):
            return 'Rio Grande do Norte'
        elif (sigla == 'RO'):
            return 'Rondônia'
        elif (sigla == 'RR'):
            return 'Roraima'
        elif (sigla == 'SP'):
            return 'São Paulo'
        elif (sigla == 'SE'):
            return 'Sergipe'
        elif (sigla == 'TO'):
            return 'Tocantins'
