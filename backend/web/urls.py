from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_user'),
    
    path('', views.Dashboard.as_view(), name='dashboard'),

]
