from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='ROH_home' ),
    path('register/', views.RegisterView.as_view(), name='ROH_Register' ),
    path('register/WRJudwR', views.registerWheelRecievedJudwListView.as_view(), name='WRJudwR')
]
