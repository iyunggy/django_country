from django import forms
from api import models

class CountryForm(forms.ModelForm):
      class Meta:
        model = models.Country
        fields = '__all__'

class CategoryForm(forms.ModelForm):
      class Meta:
        model = models.Category
        fields = '__all__'