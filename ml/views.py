import matplotlib.pyplot as plt
import numpy as np 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from math import *
from django.utils import timezone
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pdb
import requests 
from bs4 import BeautifulSoup
import smtplib
import sklearn
from django.core.files.storage import FileSystemStorage
import pandas as pd
import io 

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
    else:
        name = ''
        url = ''
    return render(request, 'ml/upload.html', {
        'name' : name, 
        'url' : url,
    })


def mlr(request):
    df = pd.read_csv('media/data(1).csv')
    return render(request, 'ml/mlr.html')
