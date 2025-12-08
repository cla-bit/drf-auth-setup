from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin view for managing CustomUser instances."""

    # Fields displayed in list view
    list_display = [
        "id",
        "email",
        "username",
        "full_name",
        "phone_number",
        "is_active",
        "is_staff",
        "is_verified",
        "is_logged_in",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_staff", "is_superuser", "is_verified"]
    search_fields = ["email", "username", "phone_number"]
    ordering = ["-created_at"]
    readonly_fields = ["created_at", "updated_at", "slug"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("username", "first_name", "last_name", "phone_number", "slug")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Status"), {"fields": ("is_logged_in", "agreement")}),
        (
            _("Important dates"),
            {"fields": ("last_login", "date_joined", "created_at", "updated_at")},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "phone_number",
                    "agreement",
                    "is_verified",
                ),
            },
        ),
    )

    def full_name(self, obj):
        return obj.get_full_name()

    full_name.short_description = "Full Name"

    def get_queryset(self, request):
        """Customize queryset if needed (optional)."""
        return super().get_queryset(request).select_related()

    def save_model(self, request, obj, form, change):
        """Ensure slug is auto-generated on save."""
        if not obj.slug:
            base = obj.username or str(obj.email).split("@")[0]
            obj.slug = base.lower()
        super().save_model(request, obj, form, change)
