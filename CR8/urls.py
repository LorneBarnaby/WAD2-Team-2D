from django.urls import path
from CR8 import views

app_name = "cr8"

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
]
