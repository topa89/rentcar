from django.contrib import admin
from .models import Auto, Category, ModelAuto, MarkAuto, Order
# Register your models here.

admin.site.register(Auto)
admin.site.register(Category)
admin.site.register(MarkAuto)
admin.site.register(ModelAuto)
admin.site.register(Order)