from django.contrib.auth.views import LoginView
from django.urls import path

app_name='accountapp'
urlpatterns=[
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('home/',LoginView.as_view(template_name='accountapp/home.html'),name='home')
]