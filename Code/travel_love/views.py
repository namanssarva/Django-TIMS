from django.shortcuts import render , redirect
from travel_love.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def travel(request):
    if request.method == "POST":
        data = request.POST
        place_image = request.FILES.get('place_image')
        place_name = data.get('place_name')
        place_description = data.get('place_description')
        Travel.objects.create(
            place_image = place_image,
            place_name = place_name,
            place_description = place_description
        )
        return redirect('/travel/')
    queryset = Travel.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(place_name__icontains = request.GET.get('search'))

    context = {'travel': queryset}
    return render(request,"travels.html",context)

@login_required(login_url="/login/")
def delete_travel(request, id):
    queryset = Travel.objects.get(id = id)
    queryset.delete()
    return redirect('/travel/')

@login_required(login_url="/login/")
def update_travel(request,id):
    queryset = Travel.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        place_image = request.FILES.get('place_image')
        place_name = data.get('place_name')
        place_description = data.get('place_description')

        queryset.place_name = place_name
        queryset.place_description = place_description

        if place_image:
            queryset.place_image = place_image
        queryset.save()
        return redirect('/travel/')

    context = {'travel': queryset}

    return render(request,"update_travels.html",context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():

            messages.error(request, "Invalid Username.")
            return redirect('/login/')
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password.")
            return redirect('/login/')
        else:
            login(request ,user)
            return redirect('/travel/')



    return render (request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already exists.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Acoount Created Sucessfully.")

        return redirect('/register/')

    return render (request, 'register.html')

