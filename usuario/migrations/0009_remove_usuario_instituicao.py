# Generated by Django 4.1.2 on 2022-12-19 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_usuario_cargo_usuario_instituicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='instituicao',
        ),
    ]
