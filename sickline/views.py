from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class SicklineHomePageView(TemplateView):
    template_name = 'sickline_home.html'


