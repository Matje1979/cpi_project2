# Generated by Django 2.1 on 2020-03-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpi', '0020_istaknuto_link_tekst_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='prijava',
            name='Tura',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
