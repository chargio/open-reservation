from django.contrib import admin

from .models import Offspring

# Register your models here.
class OffspringAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'grade', 'parent')
    list_display_links = ('id', 'first_name', 'last_name', 'parent')


admin.site.register(Offspring, OffspringAdmin)