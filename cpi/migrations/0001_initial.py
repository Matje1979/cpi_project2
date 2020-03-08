# Generated by Django 2.1 on 2020-02-03 12:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClanTima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime', models.CharField(max_length=100)),
                ('Slika', models.ImageField(default=None, upload_to='profile_pics')),
                ('Pozicija', models.CharField(default=None, max_length=100)),
                ('Position', models.CharField(blank=True, max_length=100, null=True)),
                ('Bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Bio_en', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tim',
            },
        ),
        migrations.CreateModel(
            name='Fotografija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime', models.CharField(max_length=100)),
                ('Slika', models.ImageField(default=None, upload_to='profile_pics')),
                ('Datum_objave', models.DateTimeField(default=django.utils.timezone.now)),
                ('Ime_en', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Galerija',
            },
        ),
        migrations.CreateModel(
            name='IstorijskaTura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime', models.CharField(max_length=100)),
                ('Slika', models.ImageField(default='profile_pics/gray-box.png', upload_to='profile_pics')),
                ('Datum_objave', models.DateTimeField(default=django.utils.timezone.now)),
                ('Opis', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Opis_en', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Istorijske ture',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime', models.CharField(max_length=100)),
                ('Slika', models.ImageField(default=None, upload_to='partneri_pics')),
                ('Opis', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Partneri',
            },
        ),
        migrations.CreateModel(
            name='PressClanak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Naslov', models.CharField(max_length=100)),
                ('Medij', models.CharField(default=None, max_length=80)),
                ('Slika', models.ImageField(default=None, upload_to='press_pics')),
                ('Clanak', models.FileField(blank=True, null=True, upload_to='press')),
                ('Datum_objave', models.DateTimeField(default=django.utils.timezone.now)),
                ('Naslov_en', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Press',
            },
        ),
        migrations.CreateModel(
            name='Prijava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime', models.CharField(max_length=60)),
                ('Prezime', models.CharField(max_length=60)),
                ('Email', models.EmailField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Prijave',
            },
        ),
        migrations.CreateModel(
            name='Projekat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime', models.CharField(max_length=100)),
                ('Tip', models.CharField(choices=[('Istrazivanje', 'Istrazivanje'), ('IstorijskaTura', 'IstorijskaTura'), ('prezentacija', 'prezentacija'), ('strucni skup', 'strucni skup'), ('seminar', 'seminar')], default='Istrazivanje', max_length=100)),
                ('Slika', models.ImageField(default=None, upload_to='profile_pics')),
                ('Datum_objave', models.DateTimeField(default=django.utils.timezone.now)),
                ('Ime_en', models.CharField(blank=True, max_length=100, null=True)),
                ('Opis', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Opis_en', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projekti',
            },
        ),
        migrations.CreateModel(
            name='Publikacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Naslov', models.CharField(max_length=100)),
                ('Slika', models.ImageField(default=None, upload_to='profile_pics')),
                ('Autor', models.CharField(default=None, max_length=100)),
                ('Opis', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Opis_en', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Publikacije',
            },
        ),
        migrations.CreateModel(
            name='VideoKlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime', models.CharField(max_length=100)),
                ('Video', models.FileField(blank=True, null=True, upload_to='videos')),
                ('Datum_objave', models.DateTimeField(default=django.utils.timezone.now)),
                ('Ime_en', models.CharField(blank=True, max_length=100, null=True)),
                ('Projekat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpi.Projekat')),
            ],
            options={
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.AddField(
            model_name='fotografija',
            name='Projekat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cpi.Projekat'),
        ),
    ]
