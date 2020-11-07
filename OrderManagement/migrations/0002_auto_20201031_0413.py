# Generated by Django 3.1.2 on 2020-10-31 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0003_deliverystaff'),
        ('OrderManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='assign_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.deliverystaff'),
        ),
    ]