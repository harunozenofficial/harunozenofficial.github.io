# Generated by Django 4.2.4 on 2023-08-13 09:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("matches", "0059_tweetsent_success"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TweetSent",
        ),
    ]
