# Generated by Django 2.1 on 2020-02-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpi', '0005_auto_20200211_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressclanak',
            name='Clanak_url',
            field=models.CharField(default='cpi.rs', max_length=250),
        ),
    ]
