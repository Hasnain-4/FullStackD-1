from django.shortcuts import render
from .models import Cake, Ice_cream,Chocolate,Sweets
from math import ceil

# Create your views here.

def home(request):

    cake = Cake.objects.all()
    n= len(cake)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'cake': cake}

    # icecream = Ice_cream.objects.all()
    # choco = Chocolate.objects.all()
    # sweets = Sweets.objects.all()


    return render(request,"home.html", params)

# def index(request):
#     products= Product.objects.all()
#     n= len(products)
#     nSlides= n//4 + ceil((n/4) + (n//4))
#     params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
#     return render(request,"shop/index.html", params)

def news(request):
    import requests
    import json

    response= requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-08&sortBy=publishedAt&apiKey=7f151344fc4d420b9570773b11af7cd1").text
    json_response = json.loads(response)

    auth=[]
    tit=[]
    pub=[]
    desc=[]

# print(json.dumps(json_response,indent=2))
    for item in json_response['articles']:
        auth.append(item['author'])
        tit.append(item['title'])
        pub.append(item['publishedAt'])
        desc.append(item['description'])
    # print(author,title,publishedAt )
        data = zip(auth,tit,pub,desc)

    return render(request, 'news.html',{'data':data})