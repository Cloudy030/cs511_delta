# Generated by Django 4.1.7 on 2023-03-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emission', '0002_remove_percapitaemission_totalpc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='id',
        ),
        migrations.AlterField(
            model_name='country',
            name='country_code',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
