from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

class Projekat(models.Model):
    Ime = models.CharField(max_length=100)
    TIPOVI_PROJEKATA = (
        ('Istrazivanje', 'Istrazivanje'),
        ('IstorijskaTura', 'IstorijskaTura'),
        ('prezentacija', 'prezentacija'),
        ('strucni skup', 'strucni skup'),
        ('seminar', 'seminar')    
    )
    Tip = models.CharField(default ="Istrazivanje", max_length=100, choices=TIPOVI_PROJEKATA)
    Slika = models.ImageField(default = None, upload_to='profile_pics')
    Datum_objave = models.DateTimeField(default=timezone.now)
    Ime_en = models.CharField(max_length=100, null=True, blank=True)
    Fajl = RichTextUploadingField(blank=True, null=True)
    Kratak_opis = RichTextField(blank=True, null=True)
    Kratak_opis_en = RichTextField(blank=True, null=True)
    Opis = RichTextField(blank=True, null=True)
    Opis_en = RichTextField(blank=True, null=True)
    Slika_thumbnail_1 = ImageSpecField(source="Slika",
                                       processors =[ResizeToFill(600, 500)],
                                       format="JPEG",
                                       options={"quality": 80})
    Slika_thumbnail_2 = ImageSpecField(source="Slika",
                                       processors =[ResizeToFill(200, 300)],
                                       format="JPEG",
                                       options={"quality": 80})


    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'Projekat'
        return class_name

    class Meta:
        verbose_name_plural = "Projekti"

class ProjekatPodkategorija(models.Model):
    Ime = models.CharField(max_length=100)
    Ime_en = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.Ime

    class Meta:
        verbose_name_plural = "Podkategorije Projekata"

class SadrzajProjekatPodkategorije(models.Model):
    Podkategorija = models.ForeignKey('ProjekatPodkategorija', on_delete=models.CASCADE)
    Projekat = models.ForeignKey('Projekat', on_delete=models.CASCADE)
    Opis = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sadržaji podkategorija projekata"

class IstorijskaTura(models.Model):
    Ime = models.CharField(max_length=100)
    Slika = models.ImageField(default = "profile_pics/gray-box.png", upload_to='profile_pics')
    Datum_objave = models.DateTimeField(default=timezone.now)
    Opis = RichTextField(blank=True, null=True)
    Opis_en = RichTextField(blank=True, null=True)
    Ime_en = models.CharField(max_length= 100, default='')

    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'IstorijskaTura'
        return class_name

    class Meta:
        verbose_name_plural = "Istorijske ture"

class Prijava(models.Model):
    Ime = models.CharField(max_length=60)
    Prezime = models.CharField(max_length=60)
    Email = models.EmailField(max_length=60)
    Tura = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Ime + '' + self.Prezime

    class Meta:
        verbose_name_plural = "Prijave"



class Publikacija(models.Model):
    Naslov = models.CharField(max_length=100)
    file = models.FileField(upload_to = 'publications', null=True)
    Slika = models.ImageField(default = None, upload_to='profile_pics')
    Autor = models.CharField(default=None, max_length=100)
    Opis = RichTextField(blank=True, null=True)
    Opis_en = RichTextField(blank=True, null=True)
    Datum_objave = models.DateTimeField(default=timezone.now)
    Projekat = models.ForeignKey('Projekat', on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.Naslov

    def get_cname(self):
        class_name = 'Publikacija'
        return class_name


    class Meta:
        verbose_name_plural = "Publikacije"


class Fotografija(models.Model):
    Ime = models.CharField(max_length=100)
    Slika = models.ImageField(default = None, upload_to='profile_pics')
    Projekat = models.ForeignKey('Projekat', on_delete=models.SET_NULL, blank=True, null=True)
    Datum_objave = models.DateTimeField(default=timezone.now)
    Ime_en = models.CharField(max_length=100, null=True, blank=True)
    Slika_thumbnail_1 = ImageSpecField(source="Slika",
                                       processors =[ResizeToFill(230, 230)],
                                       format="JPEG",
                                       options={"quality": 80})


    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'Fotografija'
        return class_name
    

    class Meta:
        verbose_name_plural = "Galerija"


class VideoKlip(models.Model):
    Ime = models.CharField(max_length=100)
    Projekat = models.ForeignKey('Projekat', on_delete=models.SET_NULL, blank=True, null=True)
    Video_url = models.CharField(max_length=150, null=True, blank=True)
    Video = models.FileField(upload_to='videos', null=True, blank=True)
    Datum_objave = models.DateTimeField(default=timezone.now)
    Ime_en = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'VideoKlip'
        return class_name

    class Meta:
        verbose_name_plural = "Video"

class ClanTima(models.Model):
    Ime = models.CharField(max_length=100)
    Slika = models.ImageField(default = None, upload_to='profile_pics')
    Pozicija = models.CharField(default=None, max_length=100)
    Position = models.CharField(max_length=100, null=True, blank=True)
    Bio = RichTextField(blank=True, null=True)
    Bio_en = RichTextField(blank=True, null=True)

    def get_cname(self):
        class_name = 'ClanTima'
        return class_name

    def __str__(self):
        return self.Ime

    class Meta:
        verbose_name_plural = "Tim"

class PressClanak(models.Model):
    Naslov = models.CharField(max_length=100)
    Medij = models.CharField(max_length=80, default=None)
    Slika = models.ImageField(default = None, upload_to='press_pics')
    Clanak = models.FileField(upload_to='press', null=True, blank=True)
    Clanak_url = models.CharField(max_length=250, default='#', blank=True)
    Datum_objave = models.DateTimeField(default=timezone.now)
    Naslov_en = models.CharField(max_length=100, null=True, blank=True)
    Projekat = models.ForeignKey('Projekat', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.Naslov

    def get_cname(self):
        class_name = 'PressClanak'
        return class_name

    class Meta:
        verbose_name_plural = "Press"

class Partner(models.Model):
    Ime = models.CharField(max_length=100)
    Slika = models.ImageField(default = None, upload_to='partneri_pics')
    Opis = RichTextField(blank=True, null=True)
    Opis = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'Partner'
        return class_name

    class Meta:
        verbose_name_plural = "Partneri"

class Aktuelnost(models.Model):
    Ime = models.CharField(max_length=100)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Slika = models.ImageField(default = None, upload_to='profile_pics')

    Datum_objave = models.DateTimeField(default=timezone.now)
    Kratak_opis = models.CharField(max_length=184)
    Short_description = models.CharField(max_length=184)
    Opis = RichTextField(blank=True, null=True)
    Description = RichTextField(blank=True, null=True)
    Slika_mobile = ImageSpecField(source="Slika",
                                        processors =[ResizeToFill(360, 198)],
                                        format="JPEG",
                                        options={"quality": 80})

    Slika_mobile_small = ImageSpecField(source="Slika",
                                       processors =[ResizeToFill(120, 120)],
                                       format="JPEG",
                                       options={"quality": 80})

    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'Aktuelnost'
        return class_name

    class Meta:
        verbose_name_plural = "Aktuelnosti"


class ArhivskiMaterijal(models.Model):
    Ime = models.CharField(max_length=100)
    Ime_en = models.CharField(max_length=100, null=True, blank=True)
    Slika = models.ImageField(default = None, upload_to='press_pics')
    Kratak_opis = models.CharField(max_length=184)
    Short_description = models.CharField(max_length=184)
    Datum_objave = models.DateTimeField(default=timezone.now)
    Projekat = models.ForeignKey('Projekat', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'ArhivskiMaterijal'
        return class_name

    class Meta:
        verbose_name_plural = "Arhiva"

class Izlozba(models.Model):
    Ime = models.CharField(max_length=100)
    Ime_en = models.CharField(max_length=100, null=True, blank=True)
    Slika = models.ImageField(default = None, upload_to='press_pics')
    Kratak_opis = models.CharField(max_length=184)
    Short_description = models.CharField(max_length=184)
    Datum_objave = models.DateTimeField(default=timezone.now)
    Projekat = models.ForeignKey('Projekat', on_delete=models.SET_NULL, blank=True, null=True)
    Opis = RichTextField(blank=True, null=True)
    Opis_en = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'Izlozba'
        return class_name

    class Meta:
        verbose_name_plural = "Izlozbe"

class Eksponat(models.Model):
    Ime = models.CharField(max_length=100)
    Ime_en = models.CharField(max_length=100, null=True, blank=True)
    Slika = models.ImageField(default = None, upload_to='press_pics')
    Kratak_opis = models.CharField(max_length=184)
    Short_description = models.CharField(max_length=184)
    Datum_objave = models.DateTimeField(default=timezone.now)
    Izlozba = models.ForeignKey('Projekat', on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.Ime

    def get_cname(self):
        class_name = 'Eksponat'
        return class_name

    class Meta:
        verbose_name_plural = "Eksponati"

class Istaknuto(models.Model):
    Ime = models.CharField(max_length=80)
    Ime_en = models.CharField(max_length=80)
    Slika = models.ImageField(upload_to='istaknuto')
    Link_tekst = models.CharField(max_length=20)
    Link_tekst_en = models.CharField(default="LEARN MORE", max_length=20)

    class Meta:
        verbose_name_plural = "Istaknuto"