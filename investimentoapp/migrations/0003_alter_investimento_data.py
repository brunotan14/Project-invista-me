# Generated by Django 5.1 on 2024-09-03 15:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investimentoapp', '0002_investimento_delete_investimentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investimento',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
