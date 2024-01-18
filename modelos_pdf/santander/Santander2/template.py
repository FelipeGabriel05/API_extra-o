from .colunaTitulo import Nota, ColunaTitulo
from .negociacao import Num_page, Negociacao, Observacao
from .resumo import Resumo
from .negocios import Negocio

def Santander(file, file_name):
    templateSantander = {
        "Arquivo": file_name,
        "Nota": Nota(file),
        "Titulo": ColunaTitulo(file),
        "Total_Negocios": Negocio(file),
        "Página_2": {
            "Informações": Num_page(file),
            "Negociação": Negociacao(file),
            "Observação": Observacao(file),
            "Resumo": Resumo(file)
        }
    }
    return templateSantander
