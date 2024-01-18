from .titulo import Rendimentos
from .negocios import Negocios
from .total_mercado import Total_mercado
from .operacao import Operacao
from .infoComplementar import InfoComplementar

def Template(file, file_name):
    TemplateIR = {
        "Arquivo": file_name,
        "Rendimentos": Rendimentos(file),
        "Negocios": Negocios(file),
        "Mercado": Total_mercado(file),
        "Operação": Operacao(file),
        "Informações Complementares": InfoComplementar(file)
    }
    return TemplateIR
