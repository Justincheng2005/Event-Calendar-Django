from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.event_list.as_view(), name='list'),
    path('calendar/', views.event_calendar, name='calendar'),
]