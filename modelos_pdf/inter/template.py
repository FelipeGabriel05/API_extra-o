from .titulo import Titulo, Corretora, Cliente, Banco
from .negocios import Negocios
from .resumo import Resumo
from .observacoes import Observacoes, Final_pagina
from .text import Total_page

def Inter(file, file_name):
    i = 0
    total_paginas = Total_page(file)
    num_page = 1
    extract = {
        "Arquivo": file_name
    }
    while i < total_paginas:
        print(f"Processing page {i}")
        Template_Inter = {
            "Titulo": Titulo(i, file),
            "Corretora": Corretora(i, file),
            "Cliente": Cliente(i, file),
            "Banco": Banco(i, file),
            "Negocios Realizados": Negocios(i, file),
            "Resumo": Resumo(i, file),
            "Observações": Observacoes(i, file),
            "Final_Pagina": Final_pagina(i, file)
        }
        extract[f"Pagina_{num_page}"] = Template_Inter
        num_page += 1
        i += 1
    return extract
