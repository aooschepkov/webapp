from django.shortcuts import render

def home(request):
    # Your view logic
    return render(request, 'home.html')

def workoutcalendar(request):
    # Your view logic
    return render(request, 'workoutcalendar.html')

def logworkout(request):
    # Your view logic
    return render(request, 'logworkout.html')

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

def reports(request):
    pass

