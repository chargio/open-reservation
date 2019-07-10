from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class ProfileDetailView(LoginRequiredMixin, DetailView):
    def get(self, request):
        return render(request, 'accounts/profile.html', {'user': self.request.user})
