# Generated by Django 3.2.8 on 2021-11-16 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tarefa_criado_em'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='criado_em',
            new_name='data_criacao',
        ),
    ]
