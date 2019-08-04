from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from accounts.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class ProfileDetailView(LoginRequiredMixin, DetailView):
    def get(self, request):
        return render(request, 'accounts/profile.html', {'user': self.request.user})


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home')

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
