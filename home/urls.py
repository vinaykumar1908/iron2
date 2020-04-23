from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home' ),
    path('success/', views.SuccessPageView.as_view(), name='success'),
    path('stores/', include('stores.urls')),
    path('ROH/', include('ROH.urls')),
    path('sickline/', include('sickline.urls')),
    path('yard/', include('yard.urls')),
]