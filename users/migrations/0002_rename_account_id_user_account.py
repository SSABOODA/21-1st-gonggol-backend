# Generated by Django 3.2.3 on 2021-06-11 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='account_id',
            new_name='account',
        ),
    ]
