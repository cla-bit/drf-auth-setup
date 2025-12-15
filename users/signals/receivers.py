from django.dispatch import receiver
from allauth.account.signals import email_confirmed, user_logged_in, user_logged_out



@receiver(email_confirmed)
def mark_user_as_verified(request, email_address, **kwargs):
    user = email_address.user

    if not user.is_verified:
        user.is_verified = True
        user.is_active = True  # optional but recommended
        user.save(update_fields=["is_verified", "is_active"])


@receiver(user_logged_in)
def mark_user_as_logged_in(request, email_address, **kwargs):
    user = email_address.user

    if not user.is_logged_in:
        user.is_logged_in = True
        user.save(update_fields=["is_logged_in"])


@receiver(user_logged_out)
def mark_user_as_logged_out(request, email_address, **kwargs):
    user = email_address.user

    if user.is_logged_in:
        user.is_logged_in = False
        user.save(update_fields=["is_logged_in"])