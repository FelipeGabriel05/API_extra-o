from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .template import Template

def Verifica_colecao(name_colection):
    uri = "mongodb+srv://felipegabrielgb271:felipe123@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = 'corretagem_db'
    colecoes = client[db].list_collection_names()
    
    if name_colection in colecoes:
        return True
    else:
        return False


def Main_Modalmais(file, name_file):
    uri = "mongodb+srv://felipegabrielgb271:felipe123@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))    

    try:
        client.admin.command('ping')
        print("Conexão realizada com sucesso")
        db = client['corretagem_db']
        
        if Verifica_colecao('modal_mais') == True:
            db.modal_mais.insert_one(Template(file, name_file)) 
            return True
        else:
            db.create_collection('modal_mais')
            db.modal_mais.insert_one(Template(file, name_file))
            return True
       
    except Exception as e:
        print(e)    
        return False
