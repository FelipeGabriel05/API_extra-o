import pdfplumber
from .text import Pegar_Texto
from .titulo import Titulo
from .mercado import Mercado_Vista, Mercado_Opcoes, Mercado_Futuro
from .mercado2 import Mercado_Termo, Resultados, Consolidacao

def Total_mercado(file):
    
    total_meses = 3
    negocios_mercado = {}
    with pdfplumber.open(file):
        while total_meses <= 14:
            row = Pegar_Texto(total_meses, file)
            mes = row[7].split()
            if total_meses == 14: 
                obj_mercado = {
                    "Titulo_pagina": Titulo(total_meses, file),
                    "Mercado à vista": Mercado_Vista(total_meses, file),
                    "Mercado Opções": Mercado_Opcoes(total_meses, file),
                    "Mercado Futuro": Mercado_Futuro(total_meses, file),
                    "Mercado Termo": Mercado_Termo(total_meses, file),
                    "Resultados": Resultados(total_meses, file),
                    "Consolidação do Mês": Consolidacao(total_meses, file),
                    "informação1": row[-4],
                    "informação2": f"{row[-3]} {row[-2]}"
                }
            else:
                obj_mercado = {
                    "Titulo_pagina": Titulo(total_meses, file),
                    "Mercado à vista": Mercado_Vista(total_meses, file),
                    "Mercado Opções": Mercado_Opcoes(total_meses, file),
                    "Mercado Futuro": Mercado_Futuro(total_meses, file),
                    "Mercado Termo": Mercado_Termo(total_meses, file),
                    "Resultados": Resultados(total_meses, file),
                    "Consolidação do Mês": Consolidacao(total_meses, file),
                }
            negocios_mercado[f"{mes[-1]}"] = obj_mercado
            total_meses += 1
    return negocios_mercado
