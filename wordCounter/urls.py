from django.urls import path
from . import views

app_name = 'word-count'

urlpatterns = [
    path('home/',views.home,name="home"),
    path('count/',views.counter_function,name="counter-function")
]
