from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    val = {
        'log' : 'ADDITION'
    }
    return render(request, 'add.html', val)


def sec(req):
    return HttpResponse('<em>that is second page</em>')

def result(r):
    x = r.POST['x']
    y = r.POST['y']
    res = int(x) + int(y)
    return render(r, 'result.html', {'result': res})
