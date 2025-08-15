from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('',views.index),
    path('edit',views.editstudent,name='edit'),
    path('delet',views.deletstudent,name='delet'),
    path('show',views.showstudent,name='show'),
    path('hom',views.home,name='hom'),

]
