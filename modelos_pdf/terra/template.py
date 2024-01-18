from .titulo import Nota, Corretora, Cliente
from .banco import Banco
from .negocio import Negocios
from .resumo import Dados, Resumo

def Template(file, file_name):
    templateTerra = {
        "Arquivo": file_name,
        "Nota": Nota(file),
        "Corretora": Corretora(file),
        "Cliente": Cliente(file),
        "Banco": Banco(file),
        "Total Negocios": Negocios(file),
        "Dados da Nota": Dados(file),
        "Obsevações": Resumo(file)
    }
    return templateTerra