from django import forms

from .models import Workout



class PostFormWorkout(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('title', 'text', 'num_miles', 'time_taken')