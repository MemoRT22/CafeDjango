# Generated by Django 3.2.7 on 2021-10-23 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='precio',
            field=models.IntegerField(default=150, verbose_name='Precio'),
            preserve_default=False,
        ),
    ]