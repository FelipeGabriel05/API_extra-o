# Generated by Django 4.1.13 on 2024-01-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivos_PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_arquivo', models.CharField(max_length=255)),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True)),
                ('Arquivo', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Extracao',
                'ordering': ['id'],
            },
        ),
    ]
