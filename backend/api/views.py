from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from api import models
from users.models import CustomUser
from . import serializers
import datetime
from django.db.models import Count, Q
# Create your views here.


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CountrySerializers
    queryset = models.Country.objects.all()

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(self.__class__, self).get_permissions()
    
    def get_queryset(self):
        queryset = models.Country.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(
                Q(country_name__icontains=search) |
                Q(country_currency__icontains=search) 
            )
        return queryset
  
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializers
    queryset = models.Category.objects.all()

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(self.__class__, self).get_permissions()
    
    def get_queryset(self):
        queryset = models.Category.objects.all()
        country_id = self.request.query_params.get('country_id')
        search = self.request.query_params.get('search')
        if country_id is not None:
            queryset = queryset.filter(
                Q(country_id__id=country_id) 
            )
        if search is not None:
            queryset = queryset.filter(
                Q(category_title__icontains=search) |
                Q(price_per_kilo__icontains=search) 
            )
        return queryset
    