from django.contrib import admin

from .models import User
from offsprings.models import Offspring


class OffspringInline(admin.TabularInline):
    model = Offspring


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'phone', 'offsprings_count')
    list_display_links = ('id', 'first_name', 'last_name', 'email',)

    inlines = [
        OffspringInline,
    ]


admin.site.register(User, UserAdmin)
