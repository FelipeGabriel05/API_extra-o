import pdfplumber
from .text import Pegar_texto

def Resumo_Negocios(num_page, file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        resumo = page.crop((20, 400, 300, 540))
        table_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [34, 270],
            "explicit_horizontal_lines": [450, 460, 470, 480, 490, 500, 507,
                                                516, 526, 536]
            }
        table_resumo = resumo.extract_table(table_settings)
        
        coluna_especificacao = page.crop((20, 555, 300, 640))
        especificacao_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_horizontal_lines": [555, 565, 590, 620]
        }
        table_especificacao = coluna_especificacao.extract_table(especificacao_settings)
        
        obj_resumo = {
                "Vendas_a_Vista": table_resumo[1][2],
                "Compras_a_vista": table_resumo[2][2],
                "Opcoes_vendas": table_resumo[3][2],
                "Opcoes_a_termo": table_resumo[4][2],
                "Valor_operecoes_Ctitulo": table_resumo[5][2],
                "Valor_Das_Operacoes": table_resumo[6][2],
                "Especificacoes_diversas": table_especificacao[2][1]
            }
        return obj_resumo
    
def Observacoes(num_page, file):
    with pdfplumber.open(file):
        row = Pegar_texto(num_page, file)
            
        obs = {
            "Dados_A": 'A - Posição futuro ',
            "Dados_T": 'T - Liquidação pelo Bruto',
            "Informacao_Corretora": '2 - Corretora ou pessoa vinculada atuou na contra parte. ',
            "Dados_C": 'C - Clubes e fundos de Ações',
            "Dados_I": 'I - POP',
            "Negocio": '# - Negócio direto',
            "Dados_P": 'P - Carteira Própria',
            "Dados_Liquidacao": '8 - Liquidação Institucional',
            "Dados_H": 'H - Home Broker',
            "Dados_D": 'D - Day Trade',
            "Dados_X": 'X - Box',
            "Dados_F": 'F - Cobertura',
            "Dados_Y": 'Y - Desmanche de Box',
            "Dados_B": 'B - Debêntures',
            "Dados_L": 'L - Precatório',
            "informação_adicional": row[-1]
        }
        return obs