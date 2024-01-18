from .titulo import Nota, Corretora
from .cliente import Cliente, Banco
from .negocios import Negocios
from .resumo import Resumo, Observacao
from .resumo_financeiro import Resumo_Financeiro
from .text import Total_Paginas

def Template(file, file_name):
    total_pages = Total_Paginas(file)
    i = 0
    page = 1
    extract = {
        "Arquivo": file_name
    }
    while i < total_pages:
        TemplateBradesco = {
            "Nota": Nota(i, file),
            "Corretora": Corretora(i, file),
            "Cliente": Cliente(i, file),
            "Banco": Banco(i, file),
            "Total_Negocios": Negocios(i, file),
            "Resumo dos Negocios": Resumo(i, file),
            "Observação": Observacao(i, file),
            "Resumo Financeiro": Resumo_Financeiro(i, file)
        }
        extract[f"page_{page}"] = TemplateBradesco
        page += 1
        i += 1
    return extract