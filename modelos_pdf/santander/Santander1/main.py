from .template import Santander
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from modelos_pdf.rico.main import Verifica_colecao

def Main_Santander1(file, file_name):
    uri = "mongodb+srv://email:password@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))    

    try:
        client.admin.command('ping')
        print("Conexão realizada com sucesso")
        db = client['corretagem_db']
        
        if Verifica_colecao('santander1') == True:
            db.santander1.insert_one(Santander(file, file_name)) 
            return True
        else:
            db.create_collection('santander1')
            db.santander1.insert_one(Santander(file, file_name))
            return True
    
    except Exception as e:
        print(e) 
        return False
