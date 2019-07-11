from django.shortcuts import render

# Create your views here.

from .models import Schedule
from .models import Room

# To annotate values
from django.db.models import Value


def index(request):
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
    }
    return render(request, 'schedules/index.html', context)
