from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from offsprings.models import Offspring
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from offsprings.forms import CreateOffspringForm


# Show the Offspring of the user that is making the petition, and not more
class OffspringListView(LoginRequiredMixin, ListView):
    model = Offspring

    def get_queryset(self):
        return Offspring.objects.filter(parent=self.request.user)


class OffspringCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Offspring
    # fields = ['first_name', 'last_name', 'grade']
    success_message = "%(first_name)s se creó con éxito"
    success_url = reverse_lazy('offsprings:index')
    form_class = CreateOffspringForm

    def form_valid(self, form):
        parent = self.request.user
        # Populating the parent automatically from the request object so they can create others.
        form.instance.parent = parent
        return super(OffspringCreateView, self).form_valid(form)


class OffspringUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Offspring
    fields = ['first_name']
    success_message = "%(first_name)s se actualizó con éxito"
    success_url = reverse_lazy('offsprings:index')
    template_name_suffix = '_update_form'


class OffspringDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Offspring
    success_message = "%(first_name)s se borró con éxito"
    success_url = reverse_lazy('offsprings:index')
