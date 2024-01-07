from django.contrib import admin
from candelight_website.models import RealisationsType, RealisationsProject, ProductsSubgroup, ProductsProduct,\
    ProductsInternalExternal, RealisationsPhotos


# Register your models here.
class RealisationsProjectAdmin(admin.ModelAdmin):
    list_filter = ("arrangement", "object", "category")
    list_display = ("arrangement", "object", "category")

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            storage, path = obj.image.storage, obj.image.path
            storage.delete(path)
            obj.delete()


class RealisationsTypeAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


class RealisationsPhotosAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


class ProductsInternalExternalAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


class ProductsSubgroupAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
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
admin.site.register(RealisationsType, RealisationsTypeAdmin)
admin.site.register(RealisationsPhotos, RealisationsPhotosAdmin)
admin.site.register(ProductsInternalExternal, ProductsInternalExternalAdmin)
admin.site.register(ProductsSubgroup, ProductsSubgroupAdmin)
admin.site.register(ProductsProduct, ProductsProductsAdmin)
