# Generated by Django 3.1.4 on 2020-12-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_remove_order_table_model_process_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='amount_model',
            name='operation',
            field=models.IntegerField(default=0),
        ),
    ]
