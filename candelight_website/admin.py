from django.contrib import admin
from candelight_website.models import RealisationsType, RealisationsProject, ProductsSubgroup, ProductsProduct,\
    ProductsInternalExternal


# Register your models here.
class RealisationsProjectAdmin(admin.ModelAdmin):
    list_filter = ("arrangement", "object", "category")
    list_display = ("arrangement", "object", "category")

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            storage, path = obj.image.storage, obj.image.path
            storage.delete(path)
            obj.delete()


class ProductsProductsAdmin(admin.ModelAdmin):
    list_filter = ("name", "number", "main_group", "sub_group")
    list_display = ("name", "number", "main_group", "sub_group")

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            storage, path = obj.main_image.storage, obj.main_image.path
            storage.delete(path)
            obj.delete()


admin.site.register(RealisationsProject, RealisationsProjectAdmin)
admin.site.register(RealisationsType)
admin.site.register(ProductsInternalExternal)
admin.site.register(ProductsSubgroup)
admin.site.register(ProductsProduct, ProductsProductsAdmin)
