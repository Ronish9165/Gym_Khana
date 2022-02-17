
from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.AutoField(auto_created=True,primary_key=True)
    product_name=models.CharField(max_length=200)
    product_details=models.CharField(max_length=200)
    product_price=models.CharField(max_length=500)
    product_image=models.FileField(upload_to='product_image')

    class Meta:
        db_table="product"

class Booking(models.Model):

    Mbooking_id=models.AutoField(auto_created=True,primary_key=True)

    product_name=models.ForeignKey(Products,on_delete=models.CASCADE)

    your_name=models.CharField(max_length=100)

    address=models.CharField(max_length=100)

    date = models.DateField()

    phone_number=models.CharField(max_length=50)

    location=models.CharField(max_length=100)


    class Meta:

        db_table="boking_gymequipment"