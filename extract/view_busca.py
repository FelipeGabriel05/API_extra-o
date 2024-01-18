from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId 
from django.http import JsonResponse
from pymongo import ReturnDocument
import json

class DocumentsView(APIView):
    def get(self, request, collection_url, format=None):
        try:
            uri = "mongodb+srv://your_email:your_password@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))   
            db = client['corretagem_db']
            collection = db[collection_url]
            
            if collection:
                documents = list(collection.find())
                serialized_documents = []
                for doc in documents:
                    doc['_id'] = str(doc['_id'])
                    serialized_documents.append(doc)
                return Response(serialized_documents, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Coleção não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"eror": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class ObjectIdEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)   

class DocumentView(APIView):
    def get(self, request, collection_url, object_id_url=None, format=None):
        try:
            uri = "mongodb+srv://your_email:your_password@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))   
            db = client['corretagem_db']
            collection = db[collection_url]

            object_id = ObjectId(object_id_url)
            document = collection.find_one({"_id": object_id})
                
            if document:
                document['_id'] = str(document['_id'])
                return Response(document, status=status.HTTP_200_OK)
            else:
                raise Http404
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

    def put(self, request, collection_url, object_id_url, format=None):

        try:
            fields_to_update = request.data
            
            if fields_to_update:
                uri = "mongodb+srv://your_email:your_password@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
                client = MongoClient(uri, server_api=ServerApi('1'))   
                db = client['corretagem_db']
                collection = db[collection_url]
                
                update = {'$set': {key: str(value) if isinstance(value, ObjectId) else value for key, value in fields_to_update.items()}}
                print(f"{update}")
                
                result = collection.find_one_and_update(    
                    {"_id": ObjectId(object_id_url)},   
                    update,
                    return_document=ReturnDocument.AFTER    
                )
                
                if result:
                    serialized_result = {
                        "_id": str(result["_id"]),
                        **result
                    }
                    
                    content = json.dumps(serialized_result, cls=ObjectIdEncoder)
                    
                    return JsonResponse(content, status=status.HTTP_200_OK, safe=False)
                else:
                    return Response({'error': 'Documento não encontrado'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Campos para atualização não fornecidos'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, collection_url, object_id_url, formate=None):
        try:
            uri = "mongodb+srv://your_email:your_password@cluster0.rsejnr3.mongodb.net/?retryWrites=true&w=majority"
            client = MongoClient(uri, server_api=ServerApi('1'))   
            db = client['corretagem_db']
            collection = db[collection_url]
            
            if object_id_url:
                object_id = ObjectId(object_id_url)
                result = collection.delete_one({"_id": object_id})
                
                if result.deleted_count == 1:
                    return Response({'messagem': f"Documento com id {object_id_url} deletado com sucesso"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Documento não encontrado"}, status=status.HTTP_400_BAD_REQUEST)      
            else:
                return Response({'error': "ID do documento não foi fornecido"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
