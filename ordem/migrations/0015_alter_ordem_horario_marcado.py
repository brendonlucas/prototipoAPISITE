# Generated by Django 4.1.2 on 2022-12-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordem', '0014_rename_data_solicitado_ordem_data_marcada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='horario_marcado',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
