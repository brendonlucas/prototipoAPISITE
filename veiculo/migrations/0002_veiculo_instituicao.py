# Generated by Django 3.0.8 on 2022-07-10 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0001_initial'),
        ('veiculo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='instituicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instituicao.Instituicao'),
        ),
    ]
