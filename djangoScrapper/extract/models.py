from django.db import models
import os
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
				

		if(domainExists!='true'):
			name='TRAVERSE WILL BE DONE'
			image='TRAVERSE WILL BE DONE'
			price='TRAVERSE WILL BE DONE'
			details='TRAVERSE WILL BE DONE'
			productDescription='TRAVERSE WILL BE DONE'
			review='TRAVERSE WILL BE DONE'
			productDetailsTable='TRAVERSE WILL BE DONE'

	return {'request':request,'images':image,'name':name,'price':price,'description':productDescription,'review':review}


