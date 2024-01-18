from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .template import TemplateClear

def Verifica_colecao(name_colection):
    uri = "mongodb+srv://email:password@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = 'corretagem_db'
    colecoes = client[db].list_collection_names()
    
    if name_colection in colecoes:
        return True
    else:
        return False


def Main_clear(file, name_file):
    uri = "mongodb+srv://email:password@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))    

    try:
        client.admin.command('ping')
        print("Conexão realizada com sucesso")
        db = client['corretagem_db']
        
        if Verifica_colecao('clear') == True:
            db.clear.insert_one(TemplateClear(file, name_file))
            return True
        else:
            db.create_collection('clear')
            db.clear.insert_one(TemplateClear(file, name_file))
            return True
    
    except Exception as e:
        print(e)    
        return False

