# Generated by Django 4.0.5 on 2022-06-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_champion_price_alter_champion_sell_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='champion',
            name='sell',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
