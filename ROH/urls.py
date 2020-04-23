from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ROHHomePageView.as_view(), name='ROH_home' ),
    
]
