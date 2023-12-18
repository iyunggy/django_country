from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from api import models

class LoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/login.html', {
                  'message': None,
                  'email': None,
                })

    def post(self, request, *args, **kwargs):
          email = self.request.POST.get('email')
          password = self.request.POST.get('password')
          user = authenticate(request, username=email, password=password)
          if user is not None:
              login(request, user)
              return HttpResponseRedirect(reverse_lazy('dashboard'))
          else:
              message = "Invalid email or password."
              email = email
              password = password
              return render(request, 'registration/login.html', {
                  'message': message,
                  'email': email,
                  'password': password,
                })

class Dashboard(TemplateView, LoginRequiredMixin):
  template_name = 'dashboard/index.html'

class ListCountry(ListView, LoginRequiredMixin):
    template_name = 'dashboard/country/list.html'
    model = models.Country
    context_object_name = 'lists'