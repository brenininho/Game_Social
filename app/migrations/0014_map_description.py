# Generated by Django 4.0.5 on 2022-06-30 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_map_id_map_alter_map_puuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='description',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
