from email.policy import default
# from pickletools import decimalnl_long
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ValidationError


# Create your models here.

Categories= [
    ('el', 'Electronic'),
    ('gr','Groceries'),
    ('tr','Transportion')
]
donation_list = [
    ('ka','Kabul'),
    ('He','Helmand'),
    ('Ba','Badakhshan'),
    ('Pa','Panjsher'),
    ('Gh','Ghazni')
]


class product(models.Model):
    name = models.CharField(max_length=12, unique= True)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    categories = models.CharField(max_length=12,choices=Categories, default= True)
    is_available = models.BooleanField(null= True, blank= True)
    description = models.TextField(max_length=500,default='This is description')
    create = models.DateTimeField(auto_now= True)
    update = models.DateTimeField(auto_now_add=True)


class donor(models.Model):
    name = models.CharField(unique = True,max_length=12)
    surname = models.CharField(max_length=12)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    donate_to = models.CharField(max_length=12, choices=donation_list,default= True)

class contacts(models.Model):
    firstname= models.CharField(max_length= 20)
    lastname= models.CharField(max_length=20)
    email= models.EmailField(default=False)
    address1= models.CharField(max_length=50)
    address2= models.CharField(max_length=50)
    city= models.CharField(max_length=20)
    zip=models.CharField(max_length=5)
    desc=models.TextField(max_length=700,default='This is description')
    is_true=models.BooleanField(default=False)

class contact(models.Model):
    firstname1= models.CharField(max_length= 20)
    lastname1= models.CharField(max_length=20)
    email= models.EmailField(default=False)
    address1= models.CharField(max_length=50)
    address2= models.CharField(max_length=50)
    city= models.CharField(max_length=20)
    zip=models.CharField(max_length=5)
    desc=models.TextField(max_length=700,default='This is description')
    is_true=models.BooleanField(default=False)

    
