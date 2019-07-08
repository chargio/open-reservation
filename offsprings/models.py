from django.db import models
from accounts.models import User

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
    parent = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="padre o tutor")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)