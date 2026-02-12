from django.contrib import admin

# Register your models hen
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('user_name', 'email', 'phone_number', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user_name', 'email', 'phone_number')
    ordering = ('user_name',)
    fieldsets = (
        (None, {'fields': ('user_name', 'email', 'password', 'phone_number', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'email', 'password', 'phone_number', 'is_active'),
        }),
    )

    # ✅ Remove references to missing fields
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

