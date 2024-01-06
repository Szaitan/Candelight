from django.contrib import admin
from candelight_website.models import RealisationsType, RealisationsProject, ProductsSubgroup, ProductsProduct,\
    ProductsInternalExternal


# Register your models here.
class RealisationsProjectAdmin(admin.ModelAdmin):
    list_filter = ("title", "category")
    list_display = ("title", "category")


class ProductsProductsAdmin(admin.ModelAdmin):
    list_filter = ("name", "number", "main_group", "sub_group")
    list_display = ("name", "number", "main_group", "sub_group")


admin.site.register(RealisationsProject, RealisationsProjectAdmin)
admin.site.register(RealisationsType)
admin.site.register(ProductsInternalExternal)
admin.site.register(ProductsSubgroup)
admin.site.register(ProductsProduct, ProductsProductsAdmin)
