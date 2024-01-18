from django.db import models

class Arquivos_PDF(models.Model):
    Nome_arquivo = models.CharField(max_length=120, null=False, blank=False)
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    Arquivo = models.FileField(upload_to='pdf/', null=False, blank=False)
    
    class Meta:
        verbose_name = 'extracao'
        ordering = ['id']
