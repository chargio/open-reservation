from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class ProfileDetailView(DetailView):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'accounts/profile.html', {'user': self.request.user})
