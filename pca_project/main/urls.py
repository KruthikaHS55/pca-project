from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.login_view, name='login'),
    path('slide1/', views.slide1, name='slide1'),
    path('slide2/', views.slide2, name='slide2'), 
    path('slide3/', views.slide3, name='slide3'),
    path('slide4/', views.slide4, name='slide4'),
    path('slide5/', views.slide5, name='slide5'),
    path('slide6/', views.slide6, name='slide6'),
    path('slide7/', views.slide7, name='slide7'),
    path('slide8/', views.slide8, name='slide8'),
    path('slide9/', views.slide9, name='slide9'),  
    path('slide10/', views.slide10, name='slide10'),    




    
     path('run/', views.run_pca, name='run_pca'),
  
]