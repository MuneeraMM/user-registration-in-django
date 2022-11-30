from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request,'index.html')
def regi(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone no']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # user = User.objects.create_user(username=fname,last_name=lname,password=password1,email=email)
        # user.save()
        # print('user created')
        # return redirect('/')
    # else:
    #     return render(request,'register.html')
        
        # for pass=confpass
    #     if password1 == password2:

    #         user = User.objects.create_user(username=fname,last_name=lname,password=password1,email=email)
    #         user.save()
    #         print('user created')
            
    #     else:
    #         print("Password does not matching..")
    #     return redirect('/')

    # else:
    #     return render(request,'register.html')
        if password1 == password2:
            if User.objects.filter(username=fname).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
                # print("Username already taken")
            # else:
            #     user = User.objects.create_user(username=fname,last_name=lname,password=password1,email=email)
            #     user.save()
            #     print('user created')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
                # print("Email already taken")
            else:
                user = User.objects.create_user(username=fname,last_name=lname,password=password1,email=email)
                user.save()
                print('user created')
            
        else:
            messages.info(request, 'Password does not matching.')
            # print("Password does not matching..")
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')
    
def log(request):
    return render(request,'login.html')