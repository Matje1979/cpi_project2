# Generated by Django 2.1 on 2020-03-03 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpi', '0009_auto_20200303_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressclanak',
            name='Clanak_url',
            field=models.CharField(blank=True, default='#', max_length=250),
        ),
    ]
