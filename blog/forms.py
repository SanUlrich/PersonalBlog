from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    """
    Registration form. Include Username, Email, Password1, Password2 fields.
    """
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
