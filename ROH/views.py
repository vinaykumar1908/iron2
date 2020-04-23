from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ROHHomePageView(TemplateView):
    template_name = 'ROH_home.html'


