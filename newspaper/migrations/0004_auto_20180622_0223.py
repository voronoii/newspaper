# Generated by Django 2.0.6 on 2018-06-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_auto_20180621_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
