from django.db import models

# Create your models here.

class Workout(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    exercise_name = models.CharField(max_length=100)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.exercise_name} on {self.start_time.strftime('%H:%M')}"

class FoodItem(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=200)
    calories = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()
    portion_size = models.FloatField()
