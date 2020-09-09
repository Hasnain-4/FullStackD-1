from django.urls import path,include
from .import views 

urlpatterns = [
    path('', views.home, name="home" ),
    path('news', views.news, name="news" ),
    path('contact', views.contact, name="contact" ),
    path('about', views.about, name="about" ),
]