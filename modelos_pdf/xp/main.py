from .template import Xp
from modelos_pdf.rico.main import Verifica_colecao
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def Main_xp(file, file_name):
    uri = "mongodb+srv://email:password@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))    

    try:
        client.admin.command('ping')
        print("Conexão realizada com sucesso")
        db = client['corretagem_db']
        
        if Verifica_colecao('xp') == True:
            db.xp.insert_one(Xp(file, file_name)) 
            return True
        else:
            db.create_collection('xp')
            db.xp.insert_one(Xp(file, file_name))
            return True
    
    except Exception as e:
        print(e) 
        return False
