from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class StoresHomePageView(TemplateView):
    template_name = 'stores_home.html'

