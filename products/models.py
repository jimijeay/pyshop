from django.db import models

#Create your models here.
class Product(models.Model):
    name=models.TextField()
    price=models.FloatField()
    image_url=models.CharField(max_length=2080)
    desc=models.CharField(max_length=1000)
    totalprice=models.TextField()
    summary=models.TextField(default="coooool")
    
    

class income(models.Model):
    item=models.TextField()
    quantity=models.FloatField()
    prices=models.FloatField()
    totalprices=models.FloatField()