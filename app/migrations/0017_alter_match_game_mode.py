# Generated by Django 4.0.5 on 2022-06-30 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_match_game_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='game_mode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.gamemode'),
        ),
    ]
