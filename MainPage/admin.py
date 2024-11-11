from django.contrib import admin
from .models import Product, Comment, Profile
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title","image_name")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Product,ProductAdmin)
admin.site.register(Comment)
admin.site.register(Profile)