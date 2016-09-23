from django.db import models

# Create your models here.
class Scrape(models.Model):	
	import requests
	r = requests.get("https://www.amazon.com/dp/b0042rum9g",headers={})