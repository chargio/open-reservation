from django.views.generic import ListView, DetailView
from offsprings.models import Offspring
from django.contrib.auth.mixins import LoginRequiredMixin


# Show the Offspring of the user that is making the petition, and not more
class OffspringListView(LoginRequiredMixin, ListView):
    model = Offspring

    def get_queryset(self):
        return Offspring.objects.filter(parent=self.request.user)


class OffspringSimpleView(LoginRequiredMixin, DetailView):
    model = Offspring
