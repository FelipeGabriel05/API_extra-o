from .corretora import Titulo, Corretora
from .cliente import Cliente, Banco
from .negocio import Negocios
from .negociacao import Negociacao, Observacoes
from .resumo import Resumo

def Santander(file, file_name):
    templateSantander = {
        "Arquivo": file_name,
        "Titulo": Titulo(file),
        "Corretora": Corretora(file),
        "Cliente": Cliente(file),
        "Banco": Banco(file),
        "Total_Negocios": Negocios(file),
        "Negociação": Negociacao(file),
        "Observação": Observacoes(file),
        "Resumo": Resumo(file)
    }
    return templateSantander
