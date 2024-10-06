from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('submit_report/', views.submit_report, name='submit_report'),  # Form submission route
]
