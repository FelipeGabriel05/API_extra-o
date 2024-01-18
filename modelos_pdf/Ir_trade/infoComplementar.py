import pdfplumber
from .text import Pegar_Texto
from .titulo import Titulo

def InfoComplementar(file):
    with pdfplumber.open(file):
        row = Pegar_Texto(17, file)
        whatsapp = row[-1].split('17/17')
        obj = {
            "Titulo_pagina": Titulo(17, file),
            "observação1": f"{row[7]} {row[8]} {row[9]} {row[10]} {row[11]} {row[12]}",
            "observação2": f"{row[13]} {row[14]} {row[15]}",
            "telefone": row[-3],
            "email": row[-2],
            "whatsapp": whatsapp[0] 
        }
        return obj
