from django.db import models

# Create your models here.
class crm3cust(models.Model):
    custid = models.IntegerField()
    custfname = models.CharField(max_length=100)
    custlname = models.CharField(max_length=100)
    custphone = models.IntegerField()
    custemail = models.EmailField()
    custcompany = models.CharField(max_length=100)
    custbillingstreet=models.CharField(max_length=100)
    custbillingcity=models.CharField(max_length=100)
    custbillingstate=models.CharField(max_length=100)
    custbillingcountry=models.CharField(max_length=100)
    custbillingpinzip=models.IntegerField()
    custshippingstreet=models.CharField(max_length=100)
    custshippingcity=models.CharField(max_length=100)
    custshippingstate=models.CharField(max_length=100)
    custshippingcountry=models.CharField(max_length=100)
    custshippingpinzip=models.IntegerField()


class crm3lead(models.Model):
    leadid=models.IntegerField()
    leadfname=models.CharField(max_length=100)
    leadlname=models.CharField(max_length=100)
    leadphone=models.IntegerField()
    leademail=models.EmailField()
    leadcompany = models.CharField(max_length=100)
    leadbillingstreet=models.CharField(max_length=100)
    leadbillingcity=models.CharField(max_length=100)
    leadbillingstate=models.CharField(max_length=100)
    leadbillingcountry=models.CharField(max_length=100)
    leadbillingpinzip=models.IntegerField()
    leadshippingstreet=models.CharField(max_length=100)
    leadshippingcity=models.CharField(max_length=100)
    leadshippingstate=models.CharField(max_length=100)
    leadshippingcountry=models.CharField(max_length=100)
    leadshippingpinzip=models.IntegerField()