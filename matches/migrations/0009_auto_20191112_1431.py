# Generated by Django 2.2.6 on 2019-11-12 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0008_auto_20191112_1431"),
    ]

    operations = [
        migrations.RenameField(
            model_name="match",
            old_name="away_team_link",
            new_name="away_team",
        ),
        migrations.RenameField(
            model_name="match",
            old_name="home_team_link",
            new_name="home_team",
        ),
    ]
