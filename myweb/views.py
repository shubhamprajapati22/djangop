from django.shortcuts import render
from .models import family_d

# Create your views here.
def index(request):
    imgss = family_d.objects.all()      #for fetching the all database content



    return render(request, 'index.html', {'imgs1' : imgss})
