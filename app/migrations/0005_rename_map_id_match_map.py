# Generated by Django 4.0.5 on 2022-06-27 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_item_item_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='map_id',
            new_name='map',
        ),
    ]
