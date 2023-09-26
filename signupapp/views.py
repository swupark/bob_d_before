from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse
from signupapp.forms import SignuppForm
from signupapp.models import Member


# Create your views here.
class Signupview(CreateView):
    model = Member
    form_class = SignuppForm
    template_name = 'signupapp/signup.html'
    def get_success_url(self):
        #프로필(모델)의 user pk를 넘겨줌.
        return reverse('accountapp:login')