"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gymassistant import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('workoutcalendar/', views.workoutcalendar, name='workoutcalendar'),
    path('workout_log/', views.workout_log, name='workout_log'),
    path('workout_list/', views.workout_list, name='workout_list'),
    path('workout_update/<int:pk>/', views.workout_update, name='workout_update'),
    path('workout_delete/<int:pk>/', views.workout_delete, name='workout_delete'),
    path('workoutlibrary/', views.workoutlibrary, name='workoutlibrary'),
    path('generateworkout/', views.generateworkout, name='generateworkout'),
    path('createworkout/', views.createworkout, name='createworkout'),
    path('exerciselibrary/', views.exerciselibrary, name='exerciselibrary'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('foodsearch/', views.foodsearch, name='foodsearch'),
    path('reports/', views.reports, name='reports'),
]
