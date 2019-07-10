# 
# Overriding forms from allauth

from allauth.account.forms import LoginForm
from .models import User


class MyCustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):

        return super(MyCustomLoginForm, self).login(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update(
            {'class': 'form-control  input-lg'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control  input-lg'})
