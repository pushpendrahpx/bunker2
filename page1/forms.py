import matplotlib.pyplot as plt
import numpy as np 
from django import forms
from .forms import *
from page1.models import *
from django.core.exceptions import ValidationError


class CreateList(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=200)
    link = forms.CharField(label='link', max_length=500)  
    
    
    class Meta:
        model = Info
        fields = (
            'name',
            'link'
        )


class Bunk_calc(forms.ModelForm):
    total_attend = forms.CharField(label='Total', max_length=2,)
    class_attend = forms.CharField(label='Attended', max_length=2,)
    subject = forms.CharField(label="Subject", max_length=50)
    
    class Meta:
        model = Bunk1
        fields = (
            'class_attend',
            'total_attend',
            'subject',
        )
    
    def clean_email(self):
        subject = self.cleaned_data['subject']
        if User.objects.filter(subject=subject).exists():
            raise ValidationError("Email already exists")
        return subject


class Td_create(forms.Form):
    name = forms.CharField(label="Name", max_length=200)


class MlForm(forms.ModelForm):
    points = forms.CharField(label='No. of points', max_length=3)
    m = forms.CharField(label='Slope', max_length=3)
    c = forms.CharField(label='Constant', max_length=3)



    class Meta:
        model = MlInfo
        fields = (
            'points',
            'm',
            'c',
        )


class PtForm(forms.ModelForm):
    item_link = forms.CharField(label='Item Link', max_length=200)
    item = forms.CharField(label='Item Name', max_length=200)
    email = forms.CharField(label='Your Email Id', max_length = 200)
    base_price = forms.CharField(label='Price you want', max_length=100)
        
    class Meta:
        model = PtModel1
        fields = (
            'item_link',
            'item',
            'email',
            'base_price'
        )
    