# Generated by Django 3.0.8 on 2022-07-15 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0005_auto_20220713_1452'),
        ('ordem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem',
            name='instituicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordem_inst', to='instituicao.Instituicao'),
        ),
    ]
