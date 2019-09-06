from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<int:aid>/', views.blog_page, name='blog_page'),
    path('edit/<int:aid>', views.edit_page, name='edit_page'),
    path('edit/action/', views.edit_action, name='edit_action'),
]
app_name = 'webhome'
