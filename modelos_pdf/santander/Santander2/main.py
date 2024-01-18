from .template import Santander
from modelos_pdf.rico.main import Verifica_colecao
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def Main_Santander2(file, file_name):
    uri = "mongodb+srv://felipegabrielgb271:felipe123@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))    

    try:
        client.admin.command('ping')
        print("Conexão realizada com sucesso")
        db = client['corretagem_db']
        
        if Verifica_colecao('santander2') == True:
            db.santander2.insert_one(Santander(file, file_name)) 
            return True
        else:
            db.create_collection('santander2')
            db.santander2.insert_one(Santander(file, file_name))
            return True
    
    except Exception as e:
        print(e) 
        return False
