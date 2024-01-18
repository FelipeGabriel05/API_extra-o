import pdfplumber
from .text import Pegar_texto

def Titulo(num_page, file):
    with pdfplumber.open(file) as pdf:
        row = Pegar_texto(num_page, file)
        
        informacoes_titulo = row[2].split()
        object_data = {
            'tipo_nota': row[0],
            'Nr_nota': informacoes_titulo[0],
            'Folha': informacoes_titulo[1],
            'Data_pregao': informacoes_titulo[2]
        }
        return object_data

def Corretora(num_page, file):
    with pdfplumber.open(file) as pdf:
        row = Pegar_texto(num_page, file)
        
        corretora = row[3]
        endereco = row[4]
        linha5 = row[5].split()
        info_fax = f'{linha5[1]} {linha5[2]} {linha5[3]} {linha5[4]} {linha5[5]}'
        linha6 = row[6].split()
        linha7 = row[7].split()
        linha8 = row[8].split()
        object_corretora = {
            'corretora': corretora,
            'endereco': endereco,
            "Telefone": info_fax,
            "Internet": linha6[1],
            "Sac": linha6[3],
            "C_N_P_J": linha7[1],
            'Carta': f'{linha7[-1]}',
            "Telefone2": f'{linha8[1]} {linha8[2]}',
            "Email_Ouvidoria": linha8[5]
        }
        return object_corretora
    
def Cliente(num_page, file):
    with pdfplumber.open(file) as pdf:
        row = Pegar_texto(num_page, file)
        
        total = 1
        nome = ''
        cliente = row[10].split()
        while total <= len(cliente) - 2:
            nome += f'{cliente[total]} '
            total += 1

        i = 0
        dados_cliente = row[11].split()
        endereco_cliente = ''
        while i <= len(dados_cliente) - 7:
            endereco_cliente += f'{dados_cliente[i]} '
            i += 1

        incremento = 0
        dados = row[12].split()
        continue_endereco = ''
        while incremento <= len(dados) - 4:
            continue_endereco += f'{dados[incremento]} '
            incremento += 1

        endereco_cliente = f'{endereco_cliente} {continue_endereco}'

        object_cliente = {
            "Cliente": cliente[0],
            'Nome_cliente': nome,
            "CPF_CNPJ_CVM_COB": cliente[-1],
            "Acessor": dados[-1],
            "Codigo_Cliente": f'{dados[-3]} {dados[-2]}',
            'telefone': f'{dados_cliente[-5]} {dados_cliente[-4]}',
            'endereco_cliente': endereco_cliente
        }
        return object_cliente

