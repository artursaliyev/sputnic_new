# Generated by Django 2.1.7 on 2019-03-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sputnic', '0011_auto_20190306_0530'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='sputnic',
            index=models.Index(fields=['description'], name='sputnic_spu_descrip_ad692f_idx'),
        ),
    ]
