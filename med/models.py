from django.db import models

# Create your models here.
class Customer(models.Model):
    cname = models.CharField(max_length=20)
    cid = models.CharField(max_length=20,primary_key=True)
    phno = models.BigIntegerField()
    
class Bill(models.Model):
    bid = models.IntegerField(primary_key=True)
    cid = models.ForeignKey(Customer)
    

class Medicine(models.Model):
    mid = models.IntegerField()
    name = models.CharField(max_length=20)
    price = models.IntegerField(max_length=10)


class Cart(models.Model):
    bid = models.ForeignKey(Bill)
    mid = models.ForeignKey(Medicine)
    qty = models.IntegerField()
    class Meta:
        unique_together = ("bid", "mid")

class Staff(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    
