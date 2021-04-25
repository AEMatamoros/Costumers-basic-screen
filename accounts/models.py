from django.db import models

# Create your models here.

class Costumer(models.Model):
    name= models.CharField(max_length=200, null = True)
    phone= models.CharField(max_length=200, null = True)
    email= models.CharField(max_length=200, null = True)
    date_created= models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return self.name;

class Tag(models.Model):
    name= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    Category= (('Indor','Indor'),('Outdor', 'Outdor'))

    name = models.CharField(max_length=200, null= True)
    price= models.FloatField(null=True)
    category= models.CharField(max_length=200, null= True, choices=Category)
    description= models.CharField(max_length=220, null= True, blank=True)
    date_created= models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, null= True)

    def __str__(self):
        return self.name



class Order(models.Model):
    Status =(('Pending','Pending'),('Out for Deliver','Out for Deliver'),('Delivered','Delivered'))

    costumer=models.ForeignKey(Costumer, null=True, on_delete= models.SET_NULL)
    product= models.ForeignKey(Product, null= True,on_delete= models.SET_NULL)

    date_created= models.DateTimeField(auto_now_add=True, null = True)
    status =  models.CharField(max_length=200, null= True, choices=Status)
    note = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.costumer.name + " Ordered " + self.product.name +" "+ self.status