from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from offsprings.models import Offspring
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


# Show the Offspring of the user that is making the petition, and not more
class OffspringListView(LoginRequiredMixin, ListView):
    model = Offspring

    def get_queryset(self):
        return Offspring.objects.filter(parent=self.request.user)


class OffspringCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Offspring
    success_message = "%(first_name)s se creó con éxito"
    success_url = 'offsprings/'


class OffspringUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Offspring
    fields = ['first_name']
    success_message = "%(first_name)s se actualizó con éxito"
    success_url = '/offsprings/'


class OffspringDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Offspring
    success_message = "%(first_name)s se borró con éxito"
    success_url = '/offsprings/'
