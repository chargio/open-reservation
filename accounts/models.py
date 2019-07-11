from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


# Extended User so I can add telephone and offspring data


class User(AbstractUser):
    phone = PhoneNumberField(null=True, blank=False)
    offsprings_surname = models.CharField(
        "apellidos de los catecúmenos",
        null=True,
        blank=False,
        max_length=150,
    )
    pass

    def offsprings_count(self,):
        return self.offspring_set.count()

    def __str__(self):
        return self.get_full_name()
