from .titulo import Titulo
from .resumo import Resumo
from .detalhes import Detalhes
from .observacoes import Adicional, Legenda

def Toro2(file, file_name):
    TemplateToro2 = {
        "Arquivo": file_name,
        "Titulo_Nota": Titulo(file),
        "Resumo_Nota": Resumo(file),
        "Detalhes": Detalhes(file),
        "Observações": {
            "Legenda": Legenda(file),
            "Obs_adicionais": Adicional(file)
        }
    }
    return TemplateToro2
