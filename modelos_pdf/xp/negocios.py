import pdfplumber

def Negocios(num_page, file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        colunas_negocios = page.crop((20, 180, page.width, 300))
        
        tabela_negocios = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "text",
            "explicit_vertical_lines": [40, 50, 110, 168, 225, 289, 345, 460, 475, 558]
        }
        negocios = colunas_negocios.extract_table(tabela_negocios)
        
        total = 0
        num_negocio = 1
        total_negocios = {}
        while total <= len(negocios) - 1:
            obj_negocios = {
                "C_V": negocios[total][0],
                "Mercadoria": negocios[total][2],
                "Vencimento": negocios[total][3],
                "Quantidade": negocios[total][4],
                "Preco_Ajuste": negocios[total][5],
                "Tipo_Negocio": negocios[total][7],
                "Vlr_de_OperacaoAjuste": negocios[total][8],
                "D_C": negocios[total][10],
                "Taxa_Operacional": negocios[total][11]
            }
            total_negocios[f'Negocio_{num_negocio}'] = obj_negocios
            num_negocio += 1
            total += 1
        
        return total_negocios
