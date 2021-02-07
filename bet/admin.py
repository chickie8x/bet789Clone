from django.contrib import admin

# Register your models here.
from bet.models import Category,Article

admin.site.register(Category)
admin.site.register(Article)