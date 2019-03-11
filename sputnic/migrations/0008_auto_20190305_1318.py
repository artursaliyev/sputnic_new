# Generated by Django 2.1.7 on 2019-03-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sputnic', '0007_auto_20190304_1515'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='sputnic',
            index_together=set(),
        ),
        migrations.AddIndex(
            model_name='sputnic',
            index=models.Index(fields=['title', 'description'], name='sputnic_spu_title_049aa9_idx'),
        ),
    ]
