from .titulo import Titulo, Corretora, Cliente
from .negocios import Negocios
from .resumo import Resumo_negocios
from .observacoes import Observacoes
from .text import Total_pagina

def Xp(file, file_name):
    total_page = Total_pagina(file)
    pagina_atual = 0
    num_pagina = 1
    extract = {
        "Arquivo": file_name
    }
    while pagina_atual < total_page:    
        TemplateXP = {
            "Titulo da Nota": Titulo(pagina_atual, file),
            "Corretora": Corretora(pagina_atual, file),
            "Cliente": Cliente(pagina_atual, file),
            "Negocios Realizados": Negocios(pagina_atual, file),
            "Resumo dos Negocios": Resumo_negocios(pagina_atual, file),
            "Observações": Observacoes(pagina_atual, file)
        }
        extract[f"Pagina_{num_pagina}"] = TemplateXP
        num_pagina += 1
        pagina_atual += 1

    return extract
