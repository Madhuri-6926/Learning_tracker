from django.shortcuts import render
from .models import Course

def dashboard(request):
    courses = Course.objects.all()
    return render(request, 'hello/dashboard.html', {'courses': courses})

def grid_view(request):
    return render(request, 'hello/grid.html')