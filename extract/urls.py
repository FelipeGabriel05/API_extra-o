from django.urls import path
from .views import Arquivos_PDF_APIView, Arquivo_PDF_APIView
from .view_busca import DocumentView, DocumentsView


urlpatterns = [
    path('extracoes/', Arquivos_PDF_APIView.as_view(), name='extracoes'),
    path('extracao/<int:pk>/', Arquivo_PDF_APIView.as_view(), name='extracao'),
    path('search/template=<str:collection_url>/id=<str:object_id_url>/', DocumentView.as_view(), name='search'),
    path('search_all/template=<str:collection_url>/', DocumentsView.as_view(), name='search_all')
]
