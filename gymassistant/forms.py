from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['start_time', 'end_time', 'exercise_name', 'sets', 'repetitions', 'weight']
