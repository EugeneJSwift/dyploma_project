from django.contrib import admin

# Register your models here.
from goods.models import Catigories, Products

# admin.site.register(Catigories)
# admin.site.register(Products)

@admin.register(Catigories)
class CatigoriesAdmin(admin.ModelAdmin):
    prepopulated_fields: dict[str, str] = {'slug': ('name',)}
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields: dict[str, str] = {'slug': ('name',)}



