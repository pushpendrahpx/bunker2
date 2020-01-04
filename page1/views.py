import matplotlib.pyplot as plt
import numpy as np 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
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


def index(response):
    return render(response, "page1/home1.html", {})
 

def admin(response):
    return render(response, "page1/admin.html", {})

        
def list_view(response):
    ls = Info.objects.all()
    return render(response, "page1/list.html", {"ls": ls})


def home_view(response, name):
    ls = Info.objects.get(name=name)
    return render(response, "page1/list.html", {'ls': ls})


def create(response):
    if response.method == 'POST':
        form = CreateList(response.POST)
        if form.is_valid() :
            name = form.cleaned_data['name']
            link = form.cleaned_data['link']
            t = Info(name=name, link=link)
            t.save()
            response.user.info.add(t)
    else:    
        form = CreateList()
    return render(response, 'page1/create.html', {'form': form})


def index2(request, id):
	ls = ToDo.objects.get(id=id)

	if request.method == "POST":
		if request.POST.get("save"):
			for item in ls.item_set.all():
				p = request.POST
				
				if "clicked" == p.get("c"+str(item.id)):
					item.complete = True
				else:
					item.complete = False

				if "text" + str(item.id) in p:
					item.text = p.get("text" + str(item.id))


				item.save()

		elif request.POST.get("add"):
			newItem = request.POST.get("new")
			if newItem != "":
				ls.item_set.create(text=newItem, complete=False)
			else:
				print("invalid")

	return render(request, "page1/indi.html", {"ls": ls})



def td_create(request):
    ls = ToDo.objects.all()
    if request.method == "POST":
        form = Td_create(request.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDo(name=n)
            t.save()

            return HttpResponseRedirect("/td/%i" %t.id)

    else:
        form = Td_create()

    return render(request, 'page1/tdcreate.html', {"form":form, 'ls':ls,})


def MlView(request):
    ls = MlInfo.objects.all()
    if request.method == "POST":
        form = MlForm(request.POST)
    else:
        form = MlForm()

    return render(request, 'page1/ev.html', {
        'form': form,
    })


def Mlr(request):
    ls = MlInfo.objects.all()
    if request.method == "POST":
        form = MlForm(request.POST)
        if form.is_valid():
            points = form.cleaned_data['points']
            m = form.cleaned_data['m']
            c = form.cleaned_data['c']
            a = float(m)
            b = float(c)
            p = float(points)
            np.random.seed(0)
            x = np.arange(0, p)
            x = x.reshape(1, len(x))
            N = x.shape[1]
            y = a*x + b + p*np.random.rand(1, N)
            m1 = np.random.randn(1,1)
            c1 = np.random.randn(1,1)
            learningrate = 0.001
            numiter = int(p)
            epoch = 20
            for i in range(numiter):
                dm = (2.0/N) *  -np.sum(np.multiply(x,(y - (m1*x +c1))))
                dc = (2.0/N) * -np.sum(y - (m1*x + c1))
                m1 = m1 -learningrate * dm
                c1 = c1 - learningrate * dm
                print ("no of iterations:",i)
                fig = Figure()
                plt.plot(x,y,'go')
                plt.plot(x,m1*x+c1,'r*')
                plt.ylabel('Data')
                u = m1[0][0]
                v = c1[0][0]
            t = MlInfo(points=points, m=m, c=c)
    else:
        form = MlForm()
        m = 0
        c = 0
        points = 0
        a = float(m)
        b = float(c)
        p = float(points)
        u = 0
        v = 0
        numiter = 0
    
    return render(request, 'page1/mlr.html', {
        'm': m,
        'c': c,
        'form': form,
        'm1': u,
        'c1': v,
        'p': p,
        'num': range(numiter),
    })


def PtView(request):
    ls = PtModel1.objects.all()
    if request.method == 'POST':
        form = PtForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            item_link = form.cleaned_data['item_link']
            item = form.cleaned_data['item']
            base_price = form.cleaned_data['base_price']
            t = PtModel1(email=email, item_link=item_link, item=item, base_price=base_price,)
            t.save()
            def item_price(x_link):
                URL = str(x_link)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
                }
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                price = soup.find(id='priceblock_ourprice').get_text()
                lp = []
                for i in range(2, len(price)):
                    lp.append(price[i])


                lp = remove_values_from_list(lp, ',')
                converted_price = listToString(lp)
                return converted_price
                       

            def item_title(x_link):
                URL = str(x_link)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
                }
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                title = soup.find(id='productTitle').get_text()
                title_s = title.strip()
                return title_s

            
            
            def remove_values_from_list(the_list, val):
                return [value for value in the_list if value != val]


            def listToString(s):   
                str1 = ""    
                return (str1.join(s))
                

            
            def send_mail():
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()

                server.login('madrixgaming2001@gmail.com', 'lpdzdfdsrgmaocou')

                subject = 'Amazon Price Tracker from Madrix'
                body = f"""
Price of your product '{item_title(item_link)}' is changed
New Price  : {item_price(item_link)}
Check out at {item_link}
                """
                msg = f"Subject : {subject}\n\n{body}"
                server.sendmail(
                    'madrixgaming2001@gmail.com',
                    email,
                    msg,
                    )
                print("#############")

                server.quit


            if float(item_price(item_link))>= float(base_price):
                send_mail()
    else:
        form = PtForm()
        price = ""

    return render(request, 'page1/pt.html', {
        'form' : form,
    })


def wishlist(request):
    ls = PtModel1.objects.all()
    if request.method == 'POST':
        form = PtForm(request.POST)
        if form.is_valid():
            item_link = form.cleaned_data('item_link')
            item = form.cleaned_data('item')
            item_link = form.cleaned_data('item_link')



    return render(request, 'page1/wishlist.html', {
        'ls' : ls,
    })


  