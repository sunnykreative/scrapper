from django.shortcuts import render
from django.template import RequestContext
from .models import Scrape

# Create your views here.
def index(request):
	return render(request,'home.html',{})

def api(request):

	return render(request,'api.html',{'request':request,'data':Scrape})

def contact(request):
	return render(request,'contact.html',{})	

def howitworks(request):
	return render(request,'how-it-works.html',{})

def aboutus(request):
	return render(request,'about-us.html',{})