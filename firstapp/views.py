from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def add(request):
    val = {
        'log' : 'ADDITION'
    }
    if request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        res = int(x) + int(y)
        messages.info(request, res)
        return redirect('/add/')
   
    return render(request, 'add.html', val)


def sec(req):
    return HttpResponse('<em>that is second page</em>')
  

def home(request):
    return redirect('/')
