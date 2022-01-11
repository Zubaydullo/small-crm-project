from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")