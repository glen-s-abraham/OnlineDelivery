# Generated by Django 3.1.2 on 2020-10-31 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0003_deliverystaff'),
        ('OrderManagement', '0002_auto_20201031_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='assign_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserManagement.deliverystaff'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pl', 'PLACED'), ('pr', 'PROCESSINGS'), ('od', 'OUTFORDELIVERY'), ('dr', 'DELIVERED')], default='pl', max_length=50),
        ),
    ]
