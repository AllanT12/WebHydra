# Generated by Django 4.1.2 on 2023-01-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packets', '0002_auto_20221024_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packets',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]