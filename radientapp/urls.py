from os import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('form/',views.form,name="form"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('mini_inq/',views.mini_inq, name="mini_inq"),
    path('inquiries/',views.show_inquiry,name="inquiries"),
    path('show/<str:pk>',views.show, name="show"),
]