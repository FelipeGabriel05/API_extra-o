from .titulo import Titulo, Corretora, Cliente
from .negocios import Negocios
from .resumo import Resumo
from .text import Total_paginas

def Template(file, name_file):
    total_page = Total_paginas(file)
    num_page = 0
    page = 1
    extract = {
        "Arquivo": name_file
    }
    while num_page < total_page:
        Template_Modalmais = {
            "Titulo da Nota": Titulo(num_page, file),
            "Corretora": Corretora(num_page, file),
            "Cliente": Cliente(num_page, file),
            "Negocios Realizados": Negocios(num_page, file),
            "Resumo": Resumo(num_page, file)
        }
        extract[f"Pagina_{page}"] = Template_Modalmais
        num_page += 1
        page += 1

    return extract
