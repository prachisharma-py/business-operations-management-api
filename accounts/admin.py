from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "role",
                    "phone_number",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "role",
                    "phone_number",
                ),
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
