
from django.shortcuts import render
from .models import countries

# Create your views here.

def country(request):

    counts = countries.objects.all( )


    return render(request, 'country/index.html', {'counts': counts})

    