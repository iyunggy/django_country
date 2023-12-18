from rest_framework import serializers
from api import models
from users.models import CustomUser

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

