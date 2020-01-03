from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from math import *


def bunk(response):
    if response.method == 'POST':
        boonk = Bunk_calc(response.POST)
        if boonk.is_valid():
            class_attend = str(boonk.cleaned_data['class_attend'])
            total_attend = str(boonk.cleaned_data['total_attend'])
            subject = str(boonk.cleaned_data['subject'])
            a = int(class_attend)
            b = int(total_attend)
            t = Bunk1(class_attend=class_attend, total_attend=total_attend, subject=subject)
            min_attend = ceil(b*0.75)
            percentage = (a/b)*100
            t.save()
    else:
        boonk = Bunk_calc()
        min_attend = 0
        percentage = 0
        class_attend = 0
        total_attend = 0
    return render(response, "page1/bunk.html", {
        "boonk": boonk, 
        'min_attend': min_attend, 
        'percent': percentage, 
        'class_attend': class_attend
    })
    
    
def sub_view(response, subject):
    ls = Bunk1.objects.get(subject=subject)
    return render(response, "page1/subadd.html", {'subject':subject})

def sub_add(response):
    ls = Bunk1.objects.all()
    return render(response, 'page1/subview.html', {
        'ls':ls,
        })
