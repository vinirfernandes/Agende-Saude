# Generated by Django 5.1.3 on 2025-02-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agende', '0004_clinica'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinica',
            name='latitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinica',
            name='longitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
