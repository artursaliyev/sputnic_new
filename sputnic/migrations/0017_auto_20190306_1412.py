# Generated by Django 2.1.7 on 2019-03-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sputnic', '0016_auto_20190306_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sputnic',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
