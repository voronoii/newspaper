# Generated by Django 2.0.6 on 2018-06-21 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_auto_20180622_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspaper',
            old_name='keyword',
            new_name='keywords',
        ),
    ]
