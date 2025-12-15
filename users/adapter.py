from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        """
        This controls the link sent in the verification email
        """
        return (
            f"{settings.FRONTEND_URL}"
            f"/registration/account-verify-email?"
            f"key={emailconfirmation.key}"
        )