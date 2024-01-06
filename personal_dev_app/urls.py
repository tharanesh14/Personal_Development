from personal_dev_app import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('home',views.home,name='home'),
    path('year',views.year,name='year')
]
