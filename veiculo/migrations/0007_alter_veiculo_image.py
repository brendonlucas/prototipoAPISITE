# Generated by Django 4.1.2 on 2023-01-29 20:44

from django.db import migrations, models
import veiculo.models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculo', '0006_alter_veiculo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='image',
            field=models.ImageField(blank=True, default='defaults/ic_car_image.png', null=True, upload_to=veiculo.models.upload_to_image),
        ),
    ]
