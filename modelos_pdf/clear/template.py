from .titulo import Titulo, Corretora, Cliente
from .banco import Banco, Negocios
from .resumo_Negocios import Resumo_Negocios, Observacoes
from .resumo_financeiro import Resumo_financeiro
from .text import Total_paginas

def TemplateClear(file, name_file):
    total_page = Total_paginas(file)
    extract_total = {
        "Arquivo": name_file
    }
    i = 0
    num_page = 1
    while i < total_page:
        print(f"Processing page {i}")
        TemplateClear = {
            "Titulo": Titulo(i, file),
            "Corretora": Corretora(i, file),
            "Cliente": Cliente(i, file),
            "Dados_corretora": Banco(i, file),
            "Negocios Realizados": Negocios(i, file),
            "Resumo dos Negocios": Resumo_Negocios(i, file),
            "Resumo Financeiro": Resumo_financeiro(i, file),
            "Observações": Observacoes(i, file)
        }
        extract_total[f"Page_{num_page}"] = TemplateClear
        num_page += 1
        i += 1
    return extract_total