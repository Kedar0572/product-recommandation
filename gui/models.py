from django.db import models


# Create your models here.
class Product(models.Model):

    asin = models.CharField(max_length=255, primary_key=True)
    product_id = models.IntegerField(null=True)
    title = models.TextField(null=True)
    product_type_name = models.TextField(null=True)
    brand = models.TextField(null=True)
    color = models.TextField(null=True)
    formatted_price = models.TextField(null=True)
    small_image_url = models.TextField(null=True)
    medium_image_url = models.TextField(null=True)
    large_image_url = models.TextField(null=True)

