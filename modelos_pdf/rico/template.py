from .titulo import Titulo, Corretora, Cliente
from .banco import Banco
from .negocios import Negocios
from .resumo_negocios import Resumo_Negocios, Observacoes
from .resumo_financeiro import Resumo_financeiro
from .text import Total_paginas

def Template(file, file_name):
    total = Total_paginas(file)
    i = 0
    page = 1
    extract = {
        "Arquivo": file_name
    }
    while i < total:
        TemplateRico = {
            "Titulo": Titulo(i, file),
            "Corretora": Corretora(i, file),
            "Cliente": Cliente(i, file),
            "Banco": Banco(i, file),
            "Negocios Realizados": Negocios(i, file),
            "Resumo dos Negocios": Resumo_Negocios(i, file),
            "Resumo Financeiro": Resumo_financeiro(i, file),
            "Observações": Observacoes(i, file)
        }
        extract[f"page_{page}"] = TemplateRico
        page += 1
        i += 1
    return extract