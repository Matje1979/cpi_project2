# Generated by Django 2.1 on 2020-03-18 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpi', '0015_auto_20200317_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='publikacija',
            name='file',
            field=models.FileField(null=True, upload_to='publications'),
        ),
    ]