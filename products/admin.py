from django.contrib import admin
from .models import Tag, Category, Product 

admin.site.register([Tag, Category, Product])