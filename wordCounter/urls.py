from django.urls import path
from . import views

app_name = 'word-count'

urlpatterns = [
    path('', views.home, name="home"),
    path('count/', views.counter_function, name="counter-function")
]
