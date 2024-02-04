# Register your models here.
from django.contrib import admin
from .models import Product,income

class IncomeAdmin(admin.ModelAdmin):
    list_display=('item','quantity','prices','totalprices')
    
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','totalprice')
    
admin.site.register(income,IncomeAdmin)

admin.site.register(Product,ProductAdmin)
