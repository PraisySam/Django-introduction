from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("project",views.project,name='project'),
    path("team",views.team,name='team'),
    path("idea",views.idea,name='idea')
]
