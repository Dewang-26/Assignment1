from django.db import models

# # Create your models here.
# class Product(models.Model): #product-table models-where to define table
#     name=models.CharField(max_length=50)
#     price=models.FloatField()
#     pdetails=models.CharField(max_length=200)
#     cat=models.IntegerField()
#     is_active=models.BooleanField(default=True)

class Msg(models.Model): #product-table models-where to define table
    name=models.CharField(max_length=50)
    price=models.FloatField()
    pdetails=models.CharField(max_length=200)
    cat=models.IntegerField()
    is_active=models.BooleanField(default=True)