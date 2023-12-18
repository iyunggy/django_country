from django import forms
from api import models

class CountryForm(forms.ModelForm):
      class Meta:
        model = models.Country
        fields = '__all__'