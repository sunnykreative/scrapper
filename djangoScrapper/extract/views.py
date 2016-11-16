from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse


# Create your views here.
def index(request):
	return render(request,'home.html',{})

def api(request):
	import requests
	from bs4 import BeautifulSoup
	r = requests.get(request.GET['url'],headers={'user-agent': 'Extract/0.0.1'})
	soup = BeautifulSoup(r.content, 'html.parser')
	image = soup.find_all("div", id="imgTagWrapperId")
	name = soup.find_all("span", id="productTitle")
	price = soup.find_all("span", id="priceblock_ourprice")
	details = soup.find_all("div", id="detail_bullets_id")
	productDescription = soup.find_all("div", id="productDescription")
	review = soup.find_all("table", id="histogramTable")
	productDetailsTable = soup.find_all("table", id="productDetailsTable")
	

	
	
	
	return render(request,'api.html',{'request':request,'images':image,'name':name,'price':price,'details':details,'description':productDescription,'review':review,'productDetailsTable':productDetailsTable})

def contact(request):
	return render(request,'contact.html',{})	

def howitworks(request):
	return render(request,'how-it-works.html',{})

def aboutus(request):
	return render(request,'about-us.html',{})