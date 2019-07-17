from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.LOGIN_APP.models import Users
import random, datetime, bcrypt

def index(request): #MAIN INDEX IE LOGIN INDEX
    return render(request,'LOGIN_APP/index.html')

def processRegistration(request): #REGISTRATION PROCESS ROUTE
    errors = Users.objects.validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
            return redirect('/')
    else:
        newUserPass = request.POST['password']
        newUserPassEncrypt = bcrypt.hashpw(newUserPass.encode(), bcrypt.gensalt())

        newUser = Users.objects.create(
        fname= request.POST['fname'],
        lname= request.POST['lname'],
        username= request.POST['username'],
        birthday= request.POST['birthday'],
        email= request.POST['email'],
        password= newUserPassEncrypt
           )
        request.session['user_live'] = newUser.id
        return redirect('/success')

def processLogin(request): #LOGIN PROCESS ROUTE    
    errors = Users.objects.loginVal(request.POST)
    if len(errors) > 1:
        for key, val in errors.items():
            messages.error(request, val)
            return redirect('/')
    else:
        passGiven = request.POST['password']
        userQuery = Users.objects.get(email= request.POST['email'])
        if bcrypt.checkpw(passGiven.encode(), userQuery.password.encode()):
            request.session['user_live'] = userQuery.id
            return redirect('/success' )

        else:
            messages.error(request, 'logFail')
            return redirect('/')    

def success(request): #RENDER SUCCESS, TO INFORM THE USER THAT THEY ARE IN SESSION
    liveUser = request.session['user_live']
    context ={
        'user': Users.objects.get(id = liveUser),

    }
    return render(request, 'LOGIN_APP/success.html', context)

def logout(request): #CLEAR USER IN SESSION
    request.session.clear()
    return redirect('/')

def userPage(request, userID): #FOR RENDERING A USERS PAGE
    context = {
        'thisUser': Users.objects.get(id= userID)

    }

    return render(request, "LOGIN_APP/userPage.html", context)