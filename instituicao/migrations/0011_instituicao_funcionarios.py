# Generated by Django 4.1.2 on 2022-12-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_remove_usuario_instituicao'),
        ('instituicao', '0010_remove_cargosinstituicao_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='funcionarios',
            field=models.ManyToManyField(to='usuario.usuario'),
        ),
    ]