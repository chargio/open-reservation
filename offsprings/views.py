from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView, View
from django.views.generic.edit import ProcessFormView
from offsprings.models import Offspring
from schedules.models import Schedule
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from offsprings.forms import CreateOffspringForm
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Show the Offspring of the user that is making the petition, and not more
class OffspringListView(LoginRequiredMixin, ListView):
    model = Offspring

    def get_queryset(self):
        return Offspring.objects.filter(parent=self.request.user)


class OffspringCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Offspring
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
    fields = ['first_name', 'birth_date', 'home_address', 'school', 'baptized']
    success_message = "%(first_name)s se actualizó con éxito"
    success_url = reverse_lazy('offsprings:index')
    template_name_suffix = '_update_form'

    def get_object(self):
        return get_object_or_404(Offspring, pk=self.kwargs['pk'], parent=self.request.user)


class OffspringDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Offspring
    success_message = "%(first_name)s se borró con éxito"
    success_url = reverse_lazy('offsprings:index')

    def get_object(self):
        return get_object_or_404(Offspring, pk=self.kwargs['pk'], parent=self.request.user)


class OffspringAssignmentNew(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    success_url = reverse_lazy('offsprings:index')
    success_message = "%(first_name)s se asignó al turno %(assignment)s"
    template_name = "offsprings/assignment.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OffspringAssignmentNew, self).get_context_data(
            *args, **kwargs)
        # Get offspring only for current_user
        offspring = Offspring.objects.get(
            id=self.kwargs['pk'], parent=self.request.user)

        schedules = Schedule.objects.order_by('room', 'day_of_week').all()
        used_days_of_week = Schedule.objects.values(
            "day_of_week").order_by("day_of_week").distinct()
        all_days_of_week = Schedule.DAYS_OF_WEEK
        used_starting_times = Schedule.objects.values(
            "start_time").order_by("start_time").distinct()

        # from django.db.models import Count
        # schedules.objects.anotate(reserved=Count('assignments'))

        # pdb.set_trace()
        for x in used_days_of_week:
            x['display_name'] = all_days_of_week[x['day_of_week']][1]

        context = {
            'schedules': schedules,
            'used_days_of_week': used_days_of_week,
            'used_starting_times': used_starting_times,
            'offspring': offspring,
        }
        return context


class OffspringAssignmentCreate(LoginRequiredMixin, SuccessMessageMixin, ProcessFormView, View):
    http_method_names = ['post']
    success_message = "Se asignó %(offpring)s a %(schedule)s"

    def post(self, request, *args, **kwargs):
        offspring = Offspring.objects.get(
            id=kwargs['offspring_id'], parent=request.user)
        schedule = Schedule.objects.get(id=kwargs['schedule_id'])

        if schedule.seats_available() > 0:
            offspring.assignment = schedule
            offspring.save()
            messages.success(
                request, f"Se asignó con éxito { offspring } a {schedule}")
        else:
            messages.error(request, "No ha sido posible asignar el turno")

        return redirect('offsprings:index')
