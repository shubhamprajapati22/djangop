from django.shortcuts import render
from .models import imagess

# Create your views here.
def index(request):
    img1 = imagess()
    img1.path_img = "shubham.JPG"
    img1.h = False
    img2 = imagess()
    img2.path_img = "dipak.jpg"
    img2.h = True
    img3 = imagess()
    img3.path_img = "mammi.jpg"
    img3.h = True

    imgss = [img1, img2, img3]

    return render(request, 'index.html', {'imgs1' : imgss})

def login(request):
    return render(request, 'login.html')
