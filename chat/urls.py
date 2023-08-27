from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trigger/', views.trigger, name='trigger'),
    path('trigger-event/', views.trigger_event, name='trigger_event'),
    path('<str:room_name>/', views.room, name='room'),

]