from .template import Template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def Verifica_colecao(nome_colecao):
    uri = "mongodb+srv://felipegabrielgb271:felipe123@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1')) 
    db = 'corretagem_db'
    colecoes = client[db].list_collection_names()
    
    if nome_colecao in colecoes:
        return True
    else:
        return False


def Main(file, file_name):
    uri = "mongodb+srv://felipegabrielgb271:felipe123@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))    

    try:
        client.admin.command('ping')
        print("Conexão realizada com sucesso")
        db = client['corretagem_db']
        if Verifica_colecao('terra') == True:
            db.terra.insert_one(Template(file, file_name))
            return True 
        else:
            db.create_collection('terra')
            db.terra.insert_one(Template(file, file_name))
            return True
       
    except Exception as e:
        print(e)
        return False
