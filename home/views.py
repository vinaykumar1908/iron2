from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class SuccessPageView(TemplateView):
    template_name = 'success.html'