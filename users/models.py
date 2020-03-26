from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ime = models.CharField(default = None, max_length=50)
    slika = models.ImageField(default = None, upload_to='profile_pics')
    adresa = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    misija = RichTextField(blank=True, null=True)
    misija_en = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.ime

    class Meta:
        verbose_name_plural = "Profili"
