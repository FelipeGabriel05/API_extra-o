import pdfplumber
from .text import Pegar_texto

def Titulo(num_page, file):
    row = Pegar_texto(num_page, file)
    
    linha_nota = row[0].split()
    linha_cabecalho = row[1].split()
    obj_cabecalho = {
        "Tipo_nota": f"{linha_nota[0]} {linha_nota[1]} {linha_nota[2]}",
        "Nr_nota": linha_cabecalho[0],
        "Folha": linha_cabecalho[1],
        "Data_pregao": linha_cabecalho[2]
    }
    return obj_cabecalho

def Corretora(num_page, file):
    row = Pegar_texto(num_page, file)
    
    linha_corretora = row[3].split()
    linha_corretora2 = row[5].split()
    linha_corretora3 = row[7].split()
    obj_corretora = {
        "Corretora": f"{linha_corretora[0]} {linha_corretora[1]} {linha_corretora[2]} {linha_corretora[3]}",
        "Fone": linha_corretora[-6],
        "Fax": f"{linha_corretora[-4]} {linha_corretora[-3]} {linha_corretora[-2]}",
        "CNPJ": linha_corretora[-1],
        "Numero_da_corretora": row[6],
        "Endereco": row[4],
        "Internet": linha_corretora2[1],
        "SAC": linha_corretora2[3],
        "Email": linha_corretora2[5],
        "Ouvidoria": linha_corretora3[1],
        "Email_Ouvidoria": linha_corretora3[4]
    }
    return obj_corretora

def Cliente(num_page, file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
    
        coluna_cliente = page.crop((20, 135, page.width, 170))
        tabela_cliente = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [138, 145, 155, 165],
            "explicit_vertical_lines": [32, 440, 560]
        }
        dados_cliente = coluna_cliente.extract_table(tabela_cliente)
        obj_cliente = {
            "Cliente": dados_cliente[0][1],
            "CPF_CNPJ": dados_cliente[0][2],
            "Endereco_cliente": f"{dados_cliente[1][1]} {dados_cliente[2][1]}",
            "Codigo_cliente": dados_cliente[2][2]
        }
        return obj_cliente
