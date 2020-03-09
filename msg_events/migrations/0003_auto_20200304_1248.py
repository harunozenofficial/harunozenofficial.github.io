# Generated by Django 3.0.3 on 2020-03-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0030_auto_20200304_1238'),
        ('msg_events', '0002_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='exclude_categories',
            field=models.ManyToManyField(related_name='tweet_exclude_categories', to='matches.Category'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='exclude_tournaments',
            field=models.ManyToManyField(related_name='tweet_exclude_tournaments', to='matches.Tournament'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='include_categories',
            field=models.ManyToManyField(related_name='tweet_include_categories', to='matches.Category'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='include_tournaments',
            field=models.ManyToManyField(related_name='tweet_include_tournaments', to='matches.Tournament'),
        ),
        migrations.AddField(
            model_name='webhook',
            name='exclude_categories',
            field=models.ManyToManyField(related_name='webhook_exclude_categories', to='matches.Category'),
        ),
        migrations.AddField(
            model_name='webhook',
            name='exclude_tournaments',
            field=models.ManyToManyField(related_name='webhook_exclude_tournaments', to='matches.Tournament'),
        ),
        migrations.AddField(
            model_name='webhook',
            name='include_categories',
            field=models.ManyToManyField(related_name='webhook_include_categories', to='matches.Category'),
        ),
        migrations.AddField(
            model_name='webhook',
            name='include_tournaments',
            field=models.ManyToManyField(related_name='webhook_include_tournaments', to='matches.Tournament'),
        ),
    ]