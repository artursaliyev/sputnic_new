# Generated by Django 2.1.7 on 2019-03-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sputnic', '0014_auto_20190306_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sputnic',
            name='description',
            field=models.TextField(blank=True, db_index=True),
        ),
    ]
