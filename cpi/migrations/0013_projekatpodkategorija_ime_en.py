# Generated by Django 2.1 on 2020-03-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpi', '0012_auto_20200313_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='projekatpodkategorija',
            name='Ime_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
