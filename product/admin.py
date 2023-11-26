from django.contrib import admin
from . import models

# Register your models here.


class InformtionAdmin(admin.StackedInline):
    model = models.Information



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'percentage_discount', 'off_price', 'slug' ,'show_image')
    inlines = (InformtionAdmin,)
    prepopulated_fields = {'slug':['title']}


admin.site.register(models.Size)
admin.site.register(models.Color)
