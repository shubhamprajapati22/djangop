from django.shortcuts import render
from .models import family_d

# Create your views here.
def index(request):
    img1 = family_d()
    img1.path_img = "shubham.JPG"
    img1.h = False
    img1.name = 'Shubham'
    img1.age = 22

    img2 = family_d()
    img2.path_img = "dipak.jpg"
    img2.h = True
    img2.name = 'dipak'
    img2.age = 30

    img3 = family_d()
    img3.path_img = "mammi.jpg"
    img3.h = True
    img3.name = 'Mammi'
    img3.age = 45

    imgss = [img1, img2, img3]

    return render(request, 'index.html', {'imgs1' : imgss})

def login(request):
    return render(request, 'login.html')
