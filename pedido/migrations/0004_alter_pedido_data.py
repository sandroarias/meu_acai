# Generated by Django 4.1.4 on 2023-01-02 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_cupom_alter_pedido_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 2, 15, 46, 17, 455103)),
        ),
    ]
