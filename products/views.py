from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.


#from datetime import date

# Create your views here.
def index(request):
	# fetch the current datetime
	#today = date.today()
	# send the current date to the template using the third argument of render
	products=Product.objects.all()
	#return HttpResponse('my first we with dj mosh')
	return render(request,'index.html',{'products' :products})
	
	#return render(request,'index.html')
	
def new(request):
    return HttpResponse('product then new.....')
