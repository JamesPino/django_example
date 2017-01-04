from django.db import models
from django.utils import timezone
# Create your models here.


class Workout(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    num_miles = models.FloatField(default=0)
    time_taken = models.FloatField(default=0)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def _get_average_mile(self):
        "Returns the person's full name."
        if self.time_taken == 0:
            return 0
        else:
            return self.time_taken/self.num_miles

    average_mile = property(_get_average_mile)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title