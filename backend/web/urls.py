from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_user'),
    
    path('', views.Dashboard.as_view(), name='dashboard'),

    path('country/', views.ListCountry.as_view(), name='country_list'),
    path('country/new/', views.NewCountry.as_view(), name='country_new'),
    path('country/update/<int:pk>/', views.UpdateCountry.as_view(), name='country_update'),

]
