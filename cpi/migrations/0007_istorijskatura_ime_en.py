# Generated by Django 2.1 on 2020-03-03 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpi', '0006_pressclanak_clanak_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='istorijskatura',
            name='Ime_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
