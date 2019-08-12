from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Extended User so I can add telephone and offspring data


class User(AbstractUser):
    phone = PhoneNumberField(null=True, blank=False, verbose_name="teléfono")
    offsprings_surname = models.CharField(
        "apellidos de los catecúmenos",
        null=True,
        blank=False,
        max_length=150,
    )
    father_name = models.CharField(
        "nombre completo del padre", max_length=150, default="nombre del padre")
    mother_name = models.CharField(
        "nombre completo de la madre", max_length=150, default="nombre de la madre")
    pass

    def offsprings_count(self,):
        return self.offspring_set.count()

    def __str__(self):
        return f"{self.get_full_name()} <{self.email}>"

    def validate_unique(self, *args, **kwargs):
        super(User, self).validate_unique(*args, **kwargs)
        qs = User.objects.filter(email=self.email)
        if qs.exists():
            raise ValidationError(
                {'email': ['El email no es válido o está repetido', ]})

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name = property(get_full_name)


@receiver(pre_save, sender=User)
def populate_username(sender, instance, *args, **kwargs):
    if instance.email and not instance.username:
        instance.username = instance.email
