"""Defines URL patterns for ljApp."""
from django.urls import path
from . import views
app_name = 'ljApp'

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
    path('topics/', views.topics, name ='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),

]
