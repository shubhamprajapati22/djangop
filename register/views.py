from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        flag = True

        if User.objects.filter(username=name).exists():
            print("name exist")
            messages.info(request, "name is allready used")
            flag = False



        if User.objects.filter(email=email).exists():
            messages.info(request, "email has allready used")
            print("email exist")
            flag = False

        if password != repassword:
            print("password not match")
            messages.info(request, "password not match")
            flag = False

        if flag:
            user = User.objects.create_user(first_name = name, password = repassword, email = email, username = name)
            user.save()
            
        
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "invalid username or password")


    return render(request, "register.html")



def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None and user.is_superuser == False:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "invalid username or password")



    return render(request, 'login.html')

def logout(request):
    auth.logout(request);
    return redirect('/')






