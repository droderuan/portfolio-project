from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblog'),
    path('<int:blog_id>/', views.blogdetail, name='blog_detail')
]