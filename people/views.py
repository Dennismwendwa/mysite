from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def people(request):
    return render(request, 'people/index.html')
