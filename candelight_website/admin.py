from django.contrib import admin
from candelight_website.models import RealisationsType, RealisationsProject, ProductsSubgroup, ProductsProduct,\
    ProductsInternalExternal


# Register your models here.
class RealisationsProjectAdmin(admin.ModelAdmin):
    list_filter = ("title", "category")
    list_display = ("title", "category")


admin.site.register(RealisationsProject, RealisationsProjectAdmin)
admin.site.register(RealisationsType)
admin.site.register(ProductsInternalExternal)
admin.site.register(ProductsSubgroup)
admin.site.register(ProductsProduct)
