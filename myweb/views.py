from django.shortcuts import render
from .models import UserData
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        pic = request.FILES['profile_pic']
        profile = UserData.objects.get(user=request.user)

        if profile.profileImg == 'Fpics/userpic.gif':
            profile.profileImg = pic
            profile.save();
        else:
            #messages.info(request, "pic allready exit")

            profile.profileImg.delete()
            profile.profileImg = pic
            profile.save();


    return render(request, 'index.html')
