from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def students(request):
    students = [
        {'id': 1, 'name': 'Kiran Kumar', 'age':27}
    ]
    return HttpResponse(students)
