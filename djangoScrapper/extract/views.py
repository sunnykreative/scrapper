from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def index(request):
	return render(request,'home.html',{})

def api(request):
	import requests
	from bs4 import BeautifulSoup
	r = requests.get(request.GET['url'],headers={'user-agent': 'Extract/0.0.1'})
	soup = BeautifulSoup(r.content, 'html.parser')
	images = soup.find_all('img')
	
	return render(request,'api.html',{'request':request,'images':images})

def contact(request):
	return render(request,'contact.html',{})	

def howitworks(request):
	return render(request,'how-it-works.html',{})

def aboutus(request):
	return render(request,'about-us.html',{})