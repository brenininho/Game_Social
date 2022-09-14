# Generated by Django 4.0.5 on 2022-07-03 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_item_description_alter_item_plain_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='lane',
            field=models.CharField(blank=True, choices=[('top', 'Top'), ('jungle', 'Jungle'), ('middle', 'Middle'), ('bottom', 'Bottom')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.account'),
        ),
    ]
