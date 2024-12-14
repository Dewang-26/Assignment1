from django.db import models

#create your models here.


class Msg(models.Model):
    #CAT=((1,'Mobile'),(2,'Shoes'),(3,'Clothes'))
    name=models.CharField(max_length=50,verbose_name="product Name")
    #price=models.FloatFeild()
    email=models.EmailField()
    mobile=models.BigIntegerField()
    msg=models.CharField()
    #pdetails=models.CharField(max_length=200,verbose_name="Product Detail")
    #cat=models.IntegerField(verbose_name="Category",choices=CAT)
    #is_active=models.BooleanField(default=True,verbose_name="Available")
    # def __str__(self):
    #   return self.name
    #pimage=models.ImageField(upload_to='image')

class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)