from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    def save(self, commit=True):
        user = super().save(commit=False)
        # ✅ Always enforce staff role for registered users
        user.role = "staff"
        user.is_staff = False       # ❌ cannot log in to Django admin
        user.is_superuser = False   # ❌ definitely not a superuser
        if commit:
            user.save()
        return user
