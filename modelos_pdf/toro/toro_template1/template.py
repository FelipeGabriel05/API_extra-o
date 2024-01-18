from .detalhes import Detalhes
from .observacoes import Observacoes
from .resumo import Resumo
from .titulo import Titulo

def Toro1(file, file_name):
    TemplateToro_1 = {
        "Arquivo": file_name,
        "Titulo_da_nota": Titulo(file),
        "Comprovante_BM&F_Resumo": Resumo(file),
        "Detalhes": Detalhes(file),
        "Observações": Observacoes(file) 
    }
    return TemplateToro_1
