# Generated by Django 2.1 on 2020-03-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpi', '0017_istaknuto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='istaknuto',
            options={'verbose_name_plural': 'Istaknuto'},
        ),
        migrations.AlterField(
            model_name='istaknuto',
            name='Ime',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='istaknuto',
            name='Ime_en',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='istaknuto',
            name='Link_tekst',
            field=models.CharField(max_length=15),
        ),
    ]
