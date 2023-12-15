from django.shortcuts import render, get_object_or_404, redirect
from .models import Workout, FoodItem
from .forms import WorkoutForm
from django.db.models import Sum
import json
from django.core.serializers.json import DjangoJSONEncoder
import requests
import datetime

def home(request):
    return render(request, 'home.html')

def workoutcalendar(request):
    return render(request, 'workoutcalendar.html')

def foodsearch(request):
    # if request.method == 'POST':
    #     food_item = request.POST.get('food_item')
    #     nutrition_facts = get_nutrition_facts(food_item)
    #     food_nutrients = nutrition_facts['foods'][0]['foodNutrients']
    #     nutrients = {nutrient['nutrientName']: nutrient['value'] for nutrient in food_nutrients}
    #     new_food_item = FoodItem(
    #         date=datetime.date.today(),
    #         name=nutrition_facts['foods'][0]['description'],
    #         manufacturer=nutrition_facts['foods'][0].get('brandName', 'Unknown'),
    #         calories = nutrients.get('Energy', 0),
    #         protein = nutrients.get('Protein', 0),
    #         fats = nutrients.get('Total lipid (fat)', 0),
    #         carbs = nutrients.get('Carbohydrate, by difference', 0)
    #     )
    #     new_food_item.save()
    #     return redirect('nutrition')
    # else:
        food_item = request.GET.get('food_item', '')
        nutrition_facts = get_nutrition_facts(food_item)
        return render(request, 'foodsearch.html', {'nutrition_facts': nutrition_facts})

def get_nutrition_facts(food_item):
    response = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key=uomfZPwsTH86c5uTmi6tgjgZ65BT84dAwluo8NhV&query={food_item}")
    return response.json()


def nutrition(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        calories = request.POST.get('calories')
        portion_size = request.POST.get('portion_size')
        protein = request.POST.get('protein')
        fats = request.POST.get('fats')
        carbs = request.POST.get('carbs')

        new_food_item = FoodItem(
            date=datetime.date.today(),
            product_name=product_name,
            calories=calories,
            portion_size=portion_size,
            protein=protein,
            fats=fats,
            carbs=carbs
        )
        new_food_item.save()
        return redirect('food_list')
    else:
        return render(request, 'nutrition.html')

    
def food_list(request):
    food_items = FoodItem.objects.all().order_by('-date')
    return render(request, 'food_list.html', {'food_items': food_items})

def food_detail(request, id):
    food_item = get_object_or_404(FoodItem, id=id)
    return render(request, 'food_detail.html', {'food_item': food_item})
    
def delete_food_item(request, id):
    food_item = get_object_or_404(FoodItem, id=id)
    if request.method == 'POST':
        food_item.delete()
        return redirect('food_list')
    else:
        return render(request, 'delete_food_item.html', {'food_item': food_item})
    
def edit_food_item(request, id):
    food_item = get_object_or_404(FoodItem, id=id)
    if request.method == 'POST':
        # ... code ...
        food_item.save()
        return redirect('food_list')
    else:
        # Render the form with the current details of the food itemx
        return render(request, 'edit_food_item.html', {'food_item': food_item})

# def nutrition_by_date(request,date):
#     date_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
#     food_items = FoodItem.objects.filter(date=date_object)
#     return render(request, 'nutrition.html', {'food_items': food_items})

def workoutlibrary(request):
    pass

def generateworkout(request):
    pass

def createworkout(request):
    pass

def exerciselibrary(request):
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