import os
from tabnanny import verbose
from django.conf import settings 
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m', null=True, blank=True)

    @staticmethod
    def resize_image(image):
        img_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        img_pil = Image.open(img_full_path)
        new_img  = img_pil.resize((400,500), Image.LANCZOS)
        new_img.save(img_full_path, optimize=True, quality=50)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            self.resize_image(self.image)

    def __str__(self):
        return self.name

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total =models.FloatField()
    quantity = models.PositiveIntegerField()
    owner  = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário')
    order_id = models.CharField(max_length=50)

    def saveOrder(self):
        self.save()
    
    




    