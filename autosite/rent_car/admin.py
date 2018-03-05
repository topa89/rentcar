from django.contrib import admin
from .models import Auto, Category, MarkAuto, Order, AutoImage


class AutoImageInline(admin.TabularInline):
    model = AutoImage

class AutoImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in AutoImage._meta.fields]
 

    class Meta:
        model = AutoImage

class AutoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Auto._meta.fields]
    inlines = [AutoImageInline]

    class Meta:
        model = Auto

admin.site.register(Auto, AutoAdmin)
admin.site.register(Category)
admin.site.register(MarkAuto)
admin.site.register(Order)
admin.site.register(AutoImage, AutoImageAdmin)