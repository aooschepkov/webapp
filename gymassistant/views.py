from django.shortcuts import render, get_object_or_404, redirect
from .models import Workout
from .forms import WorkoutForm
from django.db.models import Sum
import json
from django.core.serializers.json import DjangoJSONEncoder

def home(request):
    # Your view logic
    return render(request, 'home.html')

def workoutcalendar(request):
    # Your view logic
    return render(request, 'workoutcalendar.html')

def workoutlibrary(request):
    pass

def generateworkout(request):
    pass

def createworkout(request):
    pass

def exerciselibrary(request):
    pass

def nutrition(request):
    pass

def foodsearch(request):
    pass


def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workout_list.html', {'workouts': workouts})  #workouts/

def workout_log(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'workout_form.html', {'form': form})

def workout_update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workout_form.html', {'form': form})

def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'workout_confirm_delete.html', {'workout': workout})

def reports(request):
    workouts = Workout.objects.values('exercise_name').annotate(
        total_sets=Sum('sets'),
        total_reps=Sum('repetitions'),
        total_weight=Sum('weight')
    ).order_by('exercise_name')
    chart_data = json.dumps(list(workouts), cls=DjangoJSONEncoder)
    return render(request, 'reports.html', {'chart_data': chart_data})