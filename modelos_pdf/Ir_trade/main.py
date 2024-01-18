from .template import Template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def Verifica_colecao(name_colection):
    uri = "mongodb+srv://felipegabrielgb271:felipe123@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = 'corretagem_db'
    colecoes = client[db].list_collection_names()
    
    if name_colection in colecoes:
        return True
    else:
        return False
    

def Main_IR(file, file_name):
    uri = "mongodb+srv://felipegabrielgb271:felipe123@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))    

    try:
        client.admin.command('ping')
        print("Conexão realizada com sucesso")
        db = client['corretagem_db']
        
        if Verifica_colecao('ir_trade') == True:
            db.ir_trade.insert_one(Template(file, file_name))
            return True 
        else:
            db.create_collection('ir_trade')
            db.ir_trade.insert_one(Template(file, file_name))
            return True
    
    except Exception as e:
        print(e)    
        return False
