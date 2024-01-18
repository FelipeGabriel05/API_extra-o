from .titulo import Titulo, Corretora, Cliente
from .resumo import Resumo
from .negocios import Negocios, Observacoes
from .text import Total_Paginas

def Extract(file, file_name):
    total_paginas = Total_Paginas(file)
    pagina = 1
    i = 0
    extract = {
        "Arquivo": file_name
    }
    while i <= total_paginas - 1:
        obj = {
            "Titulo_da_Nota": Titulo(i, file),
            "Corretora": Corretora(i, file),
            "Cliente": Cliente(i, file),
            "Negocios": Negocios(i, file),
            "Resumo_dos_Negocios": Resumo(i, file),
            "Observações": Observacoes(i, file)    
        }
        extract[f"Page_{pagina}"] = obj
        pagina += 1
        i += 1
    return extract
