from django.forms import ModelForm

from signupapp.models import Member


class SignuppForm(ModelForm):
    class Meta:
        model=Member
        fields=['name','id','pw','age','gender','issue_ls','issue_hp','issue_lk',
                'issue_lc','issue_lf','issue_vg']