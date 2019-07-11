from django import forms
from django.forms import ModelForm
from offsprings.models import Offspring


class CreateOffspringForm(ModelForm):
    class Meta:
        model = Offspring
        fields = ['first_name', 'grade']

    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade != 1:
            raise forms.ValidationError(
                'Sólo se puede dar de alta a alumnos de primero de primaria, contacte con la parroquia para dar de alta a alumnos de otros cursos', code='wrong_grade')
        return grade
