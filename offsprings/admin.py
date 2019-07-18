from django.contrib import admin

from .models import Offspring


# Register your models here.
class OffspringAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'grade',
                    'parent', 'assignment', 'baptized')
    list_display_links = ('id', 'first_name', 'last_name')


admin.site.register(Offspring, OffspringAdmin)
