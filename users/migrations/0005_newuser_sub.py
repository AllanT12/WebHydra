# Generated by Django 4.1.2 on 2023-01-29 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
        ('users', '0004_alter_newuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='sub',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subscriptions.subscriptions'),
        ),
    ]
