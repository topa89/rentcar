from django.contrib import admin
from .models import Auto, Category, MarkAuto, AutoImage
from orders.models import Order
from news.models import News
from subscribers.models import Subscribers

class AutoImageInline(admin.TabularInline):
    model = AutoImage
class AutoImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in AutoImage._meta.fields]

    class Meta:
        model = AutoImage

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Auto._meta.fields]
    inlines = [AutoImageInline]

    class Meta:
        model = Auto

admin.site.register(Category)
admin.site.register(MarkAuto)
admin.site.register(Order)
admin.site.register(AutoImage, AutoImageAdmin)
admin.site.register(News)
admin.site.register(Subscribers)