# Generated by Django 4.1.2 on 2022-12-19 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0010_remove_cargosinstituicao_usuario_and_more'),
        ('usuario', '0007_alter_tipousuario_id_alter_usuario_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.tipousuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='instituicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_inst', to='instituicao.instituicao'),
        ),
    ]
