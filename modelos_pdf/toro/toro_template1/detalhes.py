import pdfplumber

def Detalhes(file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        coluna_detalhes = page.crop((20, 430, page.width, 500))
        detalhes_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [40, 106, 170, 230, 318, 413, 496, 566]
        }
        table_detalhes = coluna_detalhes.extract_table(detalhes_settings)
        linha14 = row[14].split()
        linha15 = row[15].split()
        
        total_negocios = {}
        num_negocio = 0
        while num_negocio <= len(table_detalhes) - 1:
            soma = num_negocio + 1
            negocio = {
                "CV": table_detalhes[num_negocio][0],
                "Vencimento": table_detalhes[num_negocio][1],
                "Quantidade": table_detalhes[num_negocio][2],
                "Preco_Ajuste": table_detalhes[num_negocio][3],
                "Tipo_de_negocio": table_detalhes[num_negocio][4],
                "Valor_Operacao": table_detalhes[num_negocio][5],
                "Taxa_Operacao": table_detalhes[num_negocio][6],
            }
            total_negocios[f"negocio_{soma}"] = negocio 
            num_negocio += 1
        
        total_detalhes = {
            "Título": linha14[0],
            "Quantidade_total_de_compra": linha14[5],
            "Preço médio compra": f"{linha14[9]} {linha15[0]}",
            "Quantidade_total_de_venda": linha14[14],
            "Preço médio venda": f"{linha14[-1]} {linha15[-1]}",
            "Total Negócios": total_negocios
        }
        
        return total_detalhes
