from django.shortcuts import render, redirect
from django.db import connection
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.contrib.auth import authenticate
from main.models import user, manager
from main.serializers import UserSerializer, ManagerSerializer
from rest_framework.decorators import api_view
from .forms import RegistrationForm, LoginForm, PasswordForm
from django.contrib import messages
from .encryption import encrypt, decrypt

cursor = connection.cursor()
global key 
key = b'ylZalYY7uLxKI98Um5fpNlOJZs_CqHNoSR3yi9k7qlM='

@api_view(['POST', 'GET'])
def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # x = form.save()
            print(form.cleaned_data)
            # {'username': 'user11', 'password': '1234'}
            password = form.cleaned_data.get('password')
            token = encrypt(password, 5)
            form.cleaned_data['password'] = token
            print(decrypt(token,26-5))
            print(form.cleaned_data)
            tutorial_serializer = UserSerializer(data=form.cleaned_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                username = form.cleaned_data.get('username')
                #messages.success(request, "New account created: ",username)
                #login(request, tutorial_serializer)
                #return redirect("main:homepage")
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                response = {"status": "Account Created"}
                return render(request = request, template_name="main/home.html", 
                context = {"response":response})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm
        return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def home(request):
    return render(request = request, template_name="main/home.html")

@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            token = encrypt(password, 5)
           
            query = cursor.execute('''SELECT password FROM main_user where username = %s''', [username])
            row = cursor.fetchone()
            print("roekn", token)
            print("AAAAAA", row[0])
            
            x = decrypt(row[0], 26-5)
            print(x)
            if x == password:
                # Redirect to a success page.
                response = username
                return render(request = request, template_name="main/panel.html", 
                context = {"userid":response})
                # return JsonResponse(response, status=status.HTTP_201_CREATED)

            else:
                # Return a 'disabled account' error message
                form = LoginForm
                return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})
    else:
        form = LoginForm
        return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})      
@api_view(['GET'])
def list(request, userid):
    #print(userid)
    creds = manager.objects.filter(userid_id=userid)
    #print(creds)
    if request.method == 'GET': 
        tutorials_serializer = ManagerSerializer(creds, many=True)
        x = ((tutorials_serializer.data))
        y = []
        for el in x:
            y.append(dict(el))
        print(y)
        #return JsonResponse(tutorials_serializer.data, safe=False)
        return render(request = request, template_name="main/panel.html", 
                context = {"response":y})
 

@api_view(['POST', 'GET'])
def addsite(request, userid):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = ManagerSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            response = {'status': 'created In'}
            return JsonResponse(response, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def panel(request):
    return redirect("main:panel")