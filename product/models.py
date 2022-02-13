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