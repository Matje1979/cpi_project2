from .models import Prijava
from django.forms import ModelForm

class PrijavaForm(ModelForm):
	class Meta:
		model = Prijava
		fields = ['Ime', 'Prezime', 'Email']
