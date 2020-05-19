from django.shortcuts import render
from .models import UserData

# Create your views here.
def index(request):
    if request.method == 'POST':
        pic = request.FILES['profile_pic']
        profile = UserData.objects.get(user=request.user)
        profile.profileImg = pic
        profile.save();

    return render(request, 'index.html')
