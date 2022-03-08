from django.urls import path
from CR8 import views

app_name = "cr8"

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('profile/<slug:username_slug>', views.profile, name='profile'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('faqs/', views.faqs, name='faqs'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout, name='logout')
]
