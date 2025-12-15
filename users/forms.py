# from django import forms
# from allauth.account.forms import SignupForm
# from phonenumber_field.formfields import PhoneNumberField
#
#
# class CustomSignUpForm(SignupForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone_number = PhoneNumberField(required=True, region="NG")
#     agreement = forms.BooleanField(required=True)
#
#     def save(self, request):
#         user = super().save(request)
#         user.first_name = self.cleaned_data.get("first_name")
#         user.last_name = self.cleaned_data.get("last_name")
#         user.phone_number = self.cleaned_data.get("phone_number")
#         user.agreement = self.cleaned_data.get("agreement")
#         user.save()
#         return user
