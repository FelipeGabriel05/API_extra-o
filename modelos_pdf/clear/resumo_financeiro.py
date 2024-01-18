import pdfplumber

def Resumo_financeiro(num_page, file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        coluna_clearing = page.crop((300, 450, 580, 509))
        clearing_settings= {
            "horizontal_strategy": "explicit",
            "vertical_strategy": "lines",    
            "horizontal_strategy": "text",
            "explicit_horizontal_lines": [460, 470, 480, 490, 500],
            "explicit_vertical_lines": [510, 545, 555]
        }
        table_clearing = coluna_clearing.extract_table(clearing_settings)
        
        if table_clearing[-1][1] == '':
            obj_clearing = {
                "Titulo_operacao": "Clearing",
                "Valor_liquido_das_operacoes": {
                    "Valor": '',
                    "DC": ''
                },
                "Taxa_de_liquidacao": {
                    "Valor":  '',
                    "DC": ''
                },
                "Taxa_de_registro": {
                    "Valor": '',
                    "DC": ''
                },
                "Total_CBLC": {
                    "Valor": '',
                    "DC": ''
                }
            }
        else:
            obj_clearing = {
                "Titulo_operacao": table_clearing[1][0],
                "Valor_liquido_das_operacoes": {
                    "Valor": table_clearing[2][1],
                    "DC": table_clearing[2][2]
                },
                "Taxa_de_liquidacao": {
                    "Valor":  table_clearing[3][1],
                    "DC": table_clearing[3][2]
                },
                "Taxa_de_registro": {
                    "Valor": table_clearing[4][1],
                    "DC": table_clearing[4][2]
                },
                "Total_CBLC": {
                    "Valor": table_clearing[5][1],
                    "DC": table_clearing[5][2]
                }
            }
        
        coluna_bolsa = page.crop((300, 509, 580, 553))
        bolsa_settings= {
            "horizontal_strategy": "explicit",
            "vertical_strategy": "lines",    
            "horizontal_strategy": "text",
            "explicit_horizontal_lines": [515, 525, 535, 545, 555],
            "explicit_vertical_lines": [525, 545, 555]
        }   
        table_bolsa = coluna_bolsa.extract_table(bolsa_settings)
        
        if table_bolsa[2][1] == '': 
            obj_bolsa = {
                "Taxa_de_termos_opcoes": {
                    "Valor": '',
                    "DC": ''
                },
                "Taxa_A_N_A": {
                    "Valor": '',
                    "DC": ''
                },
                "Emolumentos": {
                    "Valor": '',
                    "DC": ''
                },
                "Total_BOVESPA_SOMA": {
                    "Valor": '',
                    "DC": ''
                }
            }
        else:
            obj_bolsa = {
                "Taxa_de_termos_opcoes": {
                    "Valor": table_bolsa[1][1],
                    "DC": table_bolsa[1][2]
                },
                "Taxa_A_N_A": {
                    "Valor": table_bolsa[2][1],
                    "DC": table_bolsa[2][2]
                },
                "Emolumentos": {
                    "Valor": table_bolsa[3][1],
                    "DC": table_bolsa[3][2]
                },
                "Total_BOVESPA_SOMA": {
                    "Valor": table_bolsa[4][1],
                    "DC": table_bolsa[4][2]
                }
            }
        
    coluna_corretagem = page.crop((300, 554, 580, 656))        
    corretagem_settings= {
        "horizontal_strategy": "explicit",
        "vertical_strategy": "lines",    
        "horizontal_strategy": "text",
        "explicit_horizontal_lines": [515, 525, 535, 545, 555, 647, 655],
        "explicit_vertical_lines": [525, 545, 555]
    }
    table_corretagem = coluna_corretagem.extract_table(corretagem_settings)
    
    if table_corretagem[2][1] == '':
        obj_corretagem = {
            "Taxa Operacional": {
                "Valor": '',
                "DC": ''
            },
            "Execucao":  {
                "Valor": '',
                "DC": ''
            },
            "Taxa de custodia": {
                "Valor":  '',
                "DC": ''
            },
            "Impostos": {
                "Valor": '',
                "DC": ''
            },
            "IRRF": {
                "Valor": '',
                "DC": ''
            },
            "Outros": {
                "Valor": '',
                "DC": ''
            },
            "Total": {
                "Valor": '',
                "DC": "D"
            },
            "Liquido para": {
                "Valor": '',
                "DC":  '', 
            },
            "Observacao": "Observação: (1) As operações a termo não são computadas no líquido da fatura."
        }
    else:
        obj_corretagem = {
            table_corretagem[2][0]: {
                "Valor": table_corretagem[2][1],
                "DC": table_corretagem[2][2]
            },
            "Execucao":  {
                "Valor": table_corretagem[3][1],
                "DC": table_corretagem[3][2]
            },
            table_corretagem[4][0]: {
                "Valor":  table_corretagem[4][1],
                "DC": table_corretagem[4][2]
            },
            table_corretagem[5][0]: {
                "Valor": table_corretagem[5][1],
                "DC": table_corretagem[5][2]
            },
            table_corretagem[6][0]: {
                "Valor": table_corretagem[6][1],
                "DC": table_corretagem[6][2]
            },
            "Outros": {
                "Valor": table_corretagem[7][1],
                "DC": table_corretagem[7][2]
            },
            "Total": {
                "Valor": table_corretagem[9][1],
                "DC": table_corretagem[9][2]
            },
            table_corretagem[10][0]: {
                "Valor": table_corretagem[10][1],
                "DC":  table_corretagem[10][2], 
            },
            "Observacao":  table_corretagem[11][0]
        }
    
    obj_resumo = {
        "Clearing": obj_clearing,
        "Bolsa": obj_bolsa,
        f"{table_corretagem[0][0]}": obj_corretagem
    }
    return obj_resumo