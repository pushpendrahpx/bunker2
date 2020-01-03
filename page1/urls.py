from django.urls import path
from . import views
from . import bunk
from django.contrib.auth.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list_view, name='list_view'),
    path('<str:name>', views.home_view, name='home_view'),
    path('create/', views.create, name='create'),
    path('bunk/', bunk.bunk, name='bunk'),
    path('adminpanel/', views.admin, name='admin_panel'),
    path('subject/',bunk.sub_add, name='sub_add'),
    path('td/<int:id>',views.index2, name='index2'),
    path('tdcreate/',views.td_create, name='todo_create'),
    path('ml/', views.MlView, name='MlUrl'),
    path('mlr/', views.Mlr, name='MlrUrl'),
    path('pt/', views.PtView, name='PtUrl'),
    path('pt/wishlist/', views.wishlist, name='wishlist'),
]
