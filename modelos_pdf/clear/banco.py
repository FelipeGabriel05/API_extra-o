import pdfplumber

def Banco(num_page, file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        
        bloco1 = page.crop((20, 180, page.width, 200))
        table_settings1 = {
            "horizontal_strategy": "explicit",
            "vertical_strategy": "lines",
            "explicit_horizontal_lines": [180, 186, 194],
            "explicit_vertical_lines": [231, 320, 420, 533, 560]
        }
        table1 = bloco1.extract_table(table_settings1)
        
        bloco2 = page.crop((20, 200, page.width, 220))
        table_settings2 = {
            "horizontal_strategy": "explicit",
            "vertical_strategy": "lines",
            "explicit_horizontal_lines": [200, 205, 215],
            "explicit_vertical_lines": [33, 60, 140, 230, 320, 422, 530, 560]
        }
        table2 = bloco2.extract_table(table_settings2)    
        
        obj_banco = {
            "Participante_Destino_do_Repasse": table1[1][1],
            "Cliente": table1[1][2],
            "Valor": table1[1][3],
            "Custodiante": table1[1][4],
            "C_I": table1[1][5],
            "Banco": table2[1][1],
            "Agencia": table2[1][2],
            "Conta_Corrente": table2[1][3],
            "Acionista": table2[1][4],
            "Administrador": table2[1][5],
            "Complemento_Nome": table2[1][6],
            "P_Vinc": table2[1][8]
        }
        return obj_banco
    
def Negocios(num_page, file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        
        registros = page.crop((20, 250, page.width, 450))
        table_settings2 = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "text",
            "explicit_vertical_lines": [45, 88, 101, 169, 190, 330, 360, 409,
                459, 548, 555]
            }
        negocios = registros.extract_table(table_settings2)
        
        total_negocios = {}
        contagem = 0
        num_negocios = 1
        while contagem <= len(negocios) - 1:
            obj_negocios = {
                "Q": "",
                "Negociacao": negocios[contagem][0],
                "C/V": negocios[contagem][1],
                "Tipo_Mercado": negocios[contagem][2],
                "Prazo": negocios[contagem][3],
                "Especificacao_do_Titulo": negocios[contagem][4],
                "OBS": negocios[contagem][5],
                "Quantidade": negocios[contagem][6],
                "Preco_Ajuste": negocios[contagem][7],
                "Valor_Operacao_Ajuste": negocios[contagem][8],
                "D_C": negocios[contagem][9]
            }
            total_negocios[f"negocio_{num_negocios}"] = obj_negocios
            num_negocios += 1
            contagem += 1
    return total_negocios