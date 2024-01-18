from rest_framework import serializers
from .models import Arquivos_PDF

class ArquivosSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Arquivos_PDF
        fields = (
            'id',
            'Nome_arquivo',
            'Arquivo',
            'data_de_criacao'
        )
        