# Generated by Django 2.1.7 on 2019-03-06 08:36

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sputnic', '0013_auto_20190306_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='sputnic',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='sputnic',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='sputnic_spu_search__917c34_gin'),
        ),
    ]
