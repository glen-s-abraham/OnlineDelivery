# Generated by Django 3.1.2 on 2020-10-26 06:08

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
