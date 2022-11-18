# Generated by Django 3.0.8 on 2022-07-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_remove_usuario_instituicao'),
        ('instituicao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='funcionarios',
            field=models.ManyToManyField(related_name='func_inst', to='usuario.Usuario'),
        ),
    ]
