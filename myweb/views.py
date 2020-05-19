from django.shortcuts import render
from .models import userData

# Create your views here.
def index(request):
    #imgss = family_d.objects.all()      #for fetching the all database content
    u = userData.objects.get(age = 30)


    return render(request, 'index.html',{'u':u})
