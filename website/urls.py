from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('contact.html', views.contact, name='contact'),
    path('service.html', views.service, name='service'),
    path('about.html', views.about, name='about'),
    path('pricing.html', views.pricing, name='pricing'),
    path('blog.html', views.blog, name='blog'),
    path('blogdetails.html', views.blogdetails, name='blogdetails'),
]