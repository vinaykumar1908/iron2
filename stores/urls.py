from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StoresHomePageView.as_view(), name='stores_home' ),
    
]
