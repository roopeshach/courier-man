# Generated by Django 4.0.2 on 2022-02-28 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0002_chat_receiver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='sender',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='receiver',
        ),
    ]
