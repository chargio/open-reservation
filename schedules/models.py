from django.db import models
from datetime import datetime, timedelta, time


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    # DAY_OF_THE_WEEK = {
    #    '1': _(u'Monday'),
    #    '2': _(u'Tuesday'),
    #    '3': _(u'Wednesday'),
    #    '4': _(u'Thursday'),
    #    '5': _(u'Friday'),
    #    '6': _(u'Saturday'),
    #    '7': _(u'Sunday'),
    # }
    DAYS_OF_WEEK = [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.TimeField()
    duration = models.DurationField(default=timedelta(minutes=60))
    seats_reserved = models.IntegerField(default=0)
    day_of_week = models.IntegerField(
        choices=DAYS_OF_WEEK,
        default=0)

    def __str__(self):
        return "%s: %s - %s" % (
            self.get_day_of_week_display(),
            self.start_time,
            (datetime.combine(datetime.today(), self.start_time) + self.duration).time()
        )

    def seats_available(self):
        return self.room.capacity - self.seats_reserved - self.offspring_set.count()
