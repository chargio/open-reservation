from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Extended User so I can add telephone and offspring data


class User(AbstractUser):
    phone = PhoneNumberField(null=True, blank=False)
    pass
