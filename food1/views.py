from django.shortcuts import render
from .models import Cake, Ice_cream,Chocolate,Sweets

# Create your views here.

def home(request):

    cake = Cake.objects.all()
    icecream = Ice_cream.objects.all()
    choco = Chocolate.objects.all()
    sweets = Sweets.objects.all()


    return render(request, 'home.html', {'cake':cake,'icecream':icecream,'choco':choco,'sweets':sweets})