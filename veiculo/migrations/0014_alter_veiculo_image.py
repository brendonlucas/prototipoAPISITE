# Generated by Django 4.1.2 on 2023-01-29 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculo', '0013_alter_veiculo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='image',
            field=models.FileField(blank=True, upload_to='images'),
        ),
    ]