from django.urls import path
from CR8 import views

app_name = "cr8"

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='signup'), # LORNE CHANGE THE PATH TO WHAT IT SHOULD BE
]
