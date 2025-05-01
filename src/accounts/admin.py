from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomAdminChangeForm

class UserAdmin(BaseUserAdmin):
    form = CustomAdminChangeForm

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
        ('プロフィール', {'fields': (
            'username',
            'department',
            'phone_number',
            'gender',
            'birthday',
        )}),
    )

admin.site.register(User, UserAdmin)

#admin.site.register(Profile)
