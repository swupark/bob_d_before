
from django.db import models

# Create your models here.
class Member(models.Model):
    teen=18
    younger=29
    middle=64
    elder=65
    
    Male='M'
    Female='F'

    true=1
    false=0

    age_choices=[
        (teen,'청소년(13세 ~ 18세)'),
        (younger,'청년(19세 ~ 29세)'),
        (middle,'중장년(30 ~ 64세)'),
        (elder,'노년(65세 이상 ~)')
    ]
    gender_choices=[
        (Male,'남성'),
        (Female,'여성')
    ]
    choices=[
        (true,'네'),
        (false,'아니오')
    ]
    name=models.CharField(max_length=5,null=False,unique=True)
    id=models.CharField(max_length=15,null=False,unique=True,primary_key=True)
    pw=models.CharField(max_length=15,null=False,unique=False)
    age=models.IntegerField(max_length=2,choices=age_choices,default=younger)
    gender=models.CharField(max_length=1,choices=gender_choices,default=Female)
    issue_ls=models.IntegerField(max_length=1,choices=choices,default=false)
    issue_hp = models.IntegerField(max_length=1, choices=choices, default=false)
    issue_lk = models.IntegerField(max_length=1, choices=choices, default=false)
    issue_lc = models.IntegerField(max_length=1, choices=choices, default=false)
    issue_lf = models.IntegerField(max_length=1, choices=choices, default=false)
    issue_vg = models.IntegerField(max_length=1, choices=choices, default=false)
    created_at = models.DateTimeField(auto_created=True, null=True)