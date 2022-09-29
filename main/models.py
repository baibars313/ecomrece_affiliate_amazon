from distutils.command import upload
from turtle import title
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    category_name=models.CharField( max_length=100,null=False)
    cat_slug=models.CharField(max_length=100, null=True)
    category_description=models.TextField(null=False)
    image=models.ImageField(null=False, upload_to='media/')
    def __str__(self) -> str:
        return self.category_name

class Products(models.Model):
    title=models.CharField( max_length=255,null=False)
    description=models.TextField(default='descripton')
    image=models.ImageField(null=False, upload_to='media/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    product_link=models.CharField(max_length=255, null=True)
    price=models.CharField(max_length=255, null=False)

    def __str__(self) -> str:
        return self.title
    

