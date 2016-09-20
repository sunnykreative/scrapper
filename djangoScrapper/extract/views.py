from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
def index(request):
	return render(request,'home.html',{})

def api(request):
	return render(request,'api.html',{'request':request})

def contact(request):
	return render(request,'contact.html',{})	

def howitworks(request):
	return render(request,'how-it-works.html',{})

def aboutus(request):
	return render(request,'about-us.html',{})