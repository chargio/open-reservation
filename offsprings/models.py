from django.db import models
from accounts.models import User
from schedules.models import Schedule


class Offspring(models.Model):
    GRADES = [
        (1, "Primero de Primaria"),
        (2, "Segundo de Primaria"),
        (3, "Tercero de Primaria"),
        (0, "Otros"),
    ]

    first_name = models.CharField("nombre", max_length=75)
    last_name = models.CharField("apellidos", max_length=150)
    grade = models.IntegerField("curso", choices=GRADES, default=1)
    parent = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="padre o tutor")

    assignment = models.ForeignKey(
        Schedule, on_delete=models.SET_NULL, verbose_name="turno", null=True, default=None)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.last_name = self.parent.offsprings_surname
        super().save(*args, **kwargs)
