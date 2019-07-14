#
# Overriding forms from allauth to use Patternfly
#


from allauth.account.forms import LoginForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm


class MyCustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):

        return super(MyCustomLoginForm, self).login(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update(
            {'class': 'form-control  input-lg'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control  input-lg'})


class MyCustomSignupForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name',
                  'last_name', 'phone', 'offsprings_surname')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs.update(
                {'class': 'form-control  input-lg'})
