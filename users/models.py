from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from utilities.generate_custom_id import generate_custom_user_id

# Create your models here.


class CustomUser(AbstractUser):
    """User model class"""

    id = models.CharField(
        primary_key=True,
        max_length=30,
        default=generate_custom_user_id,
        editable=False,
        unique=True,
    )
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(
        blank=True,
        unique=True,
        null=True,
        verbose_name="Phone Number",
        error_messages={"unique": "Phone number already used"},
    )
    is_logged_in = models.BooleanField(default=False)
    agreement = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # required when creating superuser

    class Meta:
        indexes = [
            models.Index(fields=["username", "slug"], name="username_slug_idx"),
            models.Index(fields=["phone_number"], name="phone_number_idx"),
        ]
        verbose_name = _("Custom User")
        verbose_name_plural = _("Custom Users")
        ordering = ["-created_at"]  # newest member to oldest member (descending order)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            base = self.username or str(self.email).split("@")[0]
            self.slug = slugify(base.lower())  # Automatically create slug from username
        super().save(*args, **kwargs)

    def get_full_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username or self.email

    def __str__(self):
        return self.get_full_name()
