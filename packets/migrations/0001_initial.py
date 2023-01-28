# Generated by Django 3.2.3 on 2022-10-24 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('packetinfo', models.TextField(blank=True, db_column='packetInfo', null=True)),
                ('deviceid', models.ForeignKey(blank=True, db_column='DeviceId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='devices.devices')),
            ],
        ),
    ]
