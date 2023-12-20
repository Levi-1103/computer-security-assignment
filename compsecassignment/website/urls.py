from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('request_view/', views.request_view, name='request_view'),
    path('staff_view/', views.staff_view, name='staff_view'),
]