# Generated by Django 3.1.2 on 2020-11-07 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderManagement', '0004_auto_20201107_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='OrderManagement.order'),
        ),
    ]