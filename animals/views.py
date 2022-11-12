from .models import Animals
from django.shortcuts import render

# Create your views here.
def animals(request):

    anins = Animals.objects.all()



    return render(request, 'animals/index.html', {'anins': anins})
    

