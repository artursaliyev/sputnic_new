# Generated by Django 2.1.7 on 2019-03-07 04:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sputnic', '0017_auto_20190306_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='sputnic',
            name='json_field',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
