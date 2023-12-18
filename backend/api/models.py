from django.db import models

# Create your models here.

class Country(models.Model):
  country_name = models.CharField(max_length=255, blank=True, null=True)
  country_flag = models.URLField(max_length=255, blank=True, null=True)
  country_currency = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self) -> str:
    return self.country_name
  
class Category(models.Model):
  country_id = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
  category_title = models.CharField(max_length=255, blank=True, null=True)
  price_per_kilo = models.IntegerField(blank=True, null=True)

  def __str__(self) -> str:
    return self.country_id
