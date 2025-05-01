from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "active",
        "staff",
        "admin",
    )
    list_filter = (
        "admin",
        "active",
    )

    ordering=("email",)
    search_fields=("email",)
    filter_horizontal=()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('staff','admin',)}),
    )

admin.site.register(User)
