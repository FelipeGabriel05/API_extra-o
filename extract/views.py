from .models import Arquivos_PDF
from .serializers import ArquivosSerializers
from rest_framework import generics, status
from rest_framework.response import Response

from modelos_pdf.terra.main import Main
from modelos_pdf.clear.main import Main_clear
from modelos_pdf.modalmais.main import Main_Modalmais
from modelos_pdf.capital.main import Main_capital
from modelos_pdf.bradesco.main import Main_bradesco
from modelos_pdf.Ir_trade.main import Main_IR
from modelos_pdf.rico.main import Main_rico
from modelos_pdf.inter.main import Main_inter
from modelos_pdf.santander.Santander1.main import Main_Santander1
from modelos_pdf.santander.Santander2.main import Main_Santander2
from modelos_pdf.toro.toro_template1.main import Main_Toro1
from modelos_pdf.toro.toro_template2.main import Main_Toro2
from modelos_pdf.xp.main import Main_xp


class Arquivos_PDF_APIView(generics.ListCreateAPIView):
    queryset = Arquivos_PDF.objects.all()
    serializer_class = ArquivosSerializers
            

    def perform_create(self, serializer):
        titulo_arquivo = serializer.validated_data.get('Nome_arquivo', '')
        arquivo = self.request.FILES.get('Arquivo')
        nome_arquivo = arquivo.name
        
        def Verify(function, file, file_name):
            extract_data = function(file, file_name)
            if extract_data == True:
                serializer.save()
                return Response({'detail': 'Dados extraídos com sucesso'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail:' 'Erro ao extrair os dados'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
        
        
        if titulo_arquivo.lower() == 'terra':
            Verify(Main, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'clear':
            Verify(Main_clear, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'modalmais':
            Verify(Main_Modalmais, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'capital':
            Verify(Main_capital, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'bradesco':
            Verify(Main_bradesco, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'trade':
            Verify(Main_IR, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'rico':
            Verify(Main_rico, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'inter':
            Verify(Main_inter, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'santander1':
            Verify(Main_Santander1, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'santander2':
            Verify(Main_Santander2, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'toro1':
            Verify(Main_Toro1, arquivo, nome_arquivo)
        elif titulo_arquivo.lower() == 'toro2':
            Verify(Main_Toro2, arquivo, nome_arquivo) 
        elif titulo_arquivo.lower() == 'xp':
            Verify(Main_xp, arquivo, nome_arquivo)
        else:
            return Response({'detail': 'Nome de arquivo não é permitido.'}, status=status.HTTP_400_BAD_REQUEST)
        
class Arquivo_PDF_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Arquivos_PDF.objects.all()
    serializer_class = ArquivosSerializers
