# Generated by Django 4.2 on 2023-08-17 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_tweetlikes_tweets_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweets',
            name='likes',
        ),
    ]
