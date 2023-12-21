from django.contrib import admin
from candelight_website.models import RealisationsType, RealisationsProject


# Register your models here.
class RealisationsProjectAdmin(admin.ModelAdmin):
    list_filter = ("title", "category")
    list_display = ("title", "category")


admin.site.register(RealisationsType)
admin.site.register(RealisationsProject, RealisationsProjectAdmin)
