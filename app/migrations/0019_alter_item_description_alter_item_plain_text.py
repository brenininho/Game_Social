# Generated by Django 4.0.5 on 2022-06-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_champion_plain_text_item_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='plain_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
