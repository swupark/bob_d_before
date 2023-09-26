from django.urls import path

from accountapp.views import home, login

app_name = "accountapp"

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
]