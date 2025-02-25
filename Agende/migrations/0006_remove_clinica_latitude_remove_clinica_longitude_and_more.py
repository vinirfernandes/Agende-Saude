# Generated by Django 5.1.3 on 2025-02-24 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agende', '0005_clinica_latitude_clinica_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinica',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='clinica',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='clinica',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
