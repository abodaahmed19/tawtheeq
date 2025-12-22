from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User

admin.site.unregister(Group)
admin.site.register(Group)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "id",
        "name",
        "username",
        "email",
        "is_staff",
        "is_active",
    )

    search_fields = ("username", "name", "email")

    fieldsets = (
        ("Basic Info", {
            "fields": ("username", "password", "name", "email")
        }),
        ("Role", {
            "fields": ("role",)
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "name", "email", "role", "password1", "password2"),
        }),
    )
