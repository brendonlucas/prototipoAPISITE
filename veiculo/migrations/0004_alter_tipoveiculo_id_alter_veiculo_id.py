# Generated by Django 4.1.2 on 2022-12-01 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculo', '0003_tipoveiculo_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoveiculo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
