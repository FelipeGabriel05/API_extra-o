import pdfplumber

def Resumo_negocios(num_page, file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        
        coluna_inferior = page.crop((20, 620, page.width, 665))
        inferior = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [630, 640, 650, 660],
            "explicit_vertical_lines": [120, 130, 225, 238.5, 330, 350, 440, 460, 540, 560]
        }
        conteudo_inferior = coluna_inferior.extract_table(inferior)
        
        coluna_inferior2 = page.crop((20, 660, page.width, 710))
        inferior2 = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [675, 685, 695, 705],
            "explicit_vertical_lines": [68,80,120, 130, 170, 184 ,225, 238.5, 328, 350, 430, 460, 540, 560]
        }
        conteudo_inferior2 = coluna_inferior2.extract_table(inferior2)
        
        obj_resumo = {
            "Vendas_disponivel": conteudo_inferior[0][2],
            "Compras_disponivel": conteudo_inferior[0][6],
            "Vendas_Opcoes": conteudo_inferior[0][9],
            "Compras_Opcoes": conteudo_inferior[0][11],
            "Valor_dos_negocios": conteudo_inferior[0][14],
            "IRRF": conteudo_inferior[2][2],
            "IRRF_DayTrade": conteudo_inferior[2][6],
            "Taxa_operacional": conteudo_inferior[2][9],
            "Taxa_registro_BMeF": conteudo_inferior[2][11],
            "Taxa_BMeF": conteudo_inferior[2][14],
            "Outros_custos": conteudo_inferior2[0][6],
            "Impostos": conteudo_inferior2[0][9],
            "Ajuste_de_posicao": conteudo_inferior2[0][12],
            "Ajuste_day_trade": conteudo_inferior2[0][14],
            "Total_de_custos_operacionais": conteudo_inferior2[0][17],
            "Outros": conteudo_inferior2[2][1],
            "IRRF_operacional": conteudo_inferior2[2][3],
            "Total_Conta_investimento": conteudo_inferior2[2][9],
            "Total_Conta_Normal": conteudo_inferior2[2][12],
            "Total_liquido": conteudo_inferior2[2][14],
            "Total_liquido_da_nota":conteudo_inferior2[2][17]
        }
        return obj_resumo
