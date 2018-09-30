from django.shortcuts import render
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView


class HomeView(TemplateView):
    template_name = "demo/home.html"
