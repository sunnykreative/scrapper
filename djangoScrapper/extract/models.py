from django.db import models
import os,time
from urllib.parse import urlparse

# Create your models here.
def scrape_data(r,request):	
	import csv
	from bs4 import BeautifulSoup

	parsed_uri = urlparse(request.GET['url'])
	domain = '{uri.netloc}'.format(uri=parsed_uri)

	htmlContent = BeautifulSoup(r.content, 'html.parser')
	csvFile=os.path.abspath(os.path.dirname(__file__))+'/../static/scrapping_dataset.csv'
	with open(csvFile) as f:
		reader = csv.reader(f, delimiter=',')
		domainExists='false'
		for row in reader:
			# 0 for image 1 for name 2 is price 3 is review 4 is description 5 is domain
			if(row[5]==domain):
				domainExists = 'true';
				image=htmlContent.select(row[0]) if (row[0]!='') else ''
				name = htmlContent.select(row[1]) if (row[1]!='') else ''
				price=htmlContent.select(row[2]) if (row[2]!='') else ''
				review=htmlContent.select(row[3]) if (row[3]!='') else ''
				productDescription=htmlContent.select(row[4]) if (row[4]!='') else ''
				
				# image=row[5]
				# name = row[1]
				# price=htmlContent.select(row[2]) if (row[2]!='') else ''
				# review=htmlContent.select(row[3]) if (row[3]!='') else ''
				# productDescription=htmlContent.select(row[4]) if (row[4]!='') else ''

		# If Domain is not mentioned on the dataset
		if(domainExists!='true'):
			name=htmlContent.select('h1') if(htmlContent.select('h1')) else ''
			print(name)
			imageurl = htmlContent.find('meta', attrs={'property': 'og:image', 'content': True})
			imagenameUrl = htmlContent.find('meta', attrs={'name': 'og:image', 'content': True})
			if imageurl:
			    image = '<img class="maxWidth600" src="'+imageurl['content']+'"/>'
			elif imagenameUrl:
				image = '<img class="maxWidth600" src="'+imagenameUrl['content']+'"/>'
			else:
			    image='<img class="maxWidth600" src="/static/images/no-image.jpg"/>'

			csvFileNotExist=os.path.abspath(os.path.dirname(__file__))+'/../static/commondataset.csv'			
			with open(csvFileNotExist) as common:
				readerCommon = csv.reader(common, delimiter=',')
				price=''
				review=''
				productDescription=''
				for itemRow in readerCommon:
					# 0 for price
					try:
					    priceTest=htmlContent.select(itemRow[0])
					    if(priceTest):
					    	price = priceTest
					    
					except NameError:
					    Nochange = None


	return {'request':request,'images':image,'name':name,'price':price,'description':productDescription,'review':review}


