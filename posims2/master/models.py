from django.db import models
from django.utils import timezone


class Inventory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    # item is a part of inventory, hence foreign key
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE)

    code = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=500,default="General")
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(default='1',max_length=200) 
    count = models.FloatField(default=1) 
    date_added =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
