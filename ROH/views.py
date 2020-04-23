from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'ROH_home.html'

class RegisterView(TemplateView):
    template_name = 'ROH/Registers.html'

class registerWheelRecievedJudwListView(ListView):
    model = models.registerWheelRecievedJudw
    template_name = 'ROH/registerWheelRecievedJudw.html'



