# Generated by Django 3.2.8 on 2021-11-17 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_tarefa_data_expiracao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='prioridade',
        ),
    ]