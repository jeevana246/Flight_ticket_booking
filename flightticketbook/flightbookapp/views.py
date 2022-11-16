from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth
from flightbookapp.models import *
from django.db.models import Q

# Create your views here.

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return render(request,'flightbookapp/dashboard.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('userlogin')

    else:    
        return render(request,'flightbookapp/login.html')

def createacc(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        username = request.POST['username']
        phonenum = request.POST['phonenumber']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                print("username exists")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
                print("email already exists")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                info = personal_det(user=user,address=address, phonenum=phonenum)
                info.save()
                print("created successfully")
                return  redirect('userlogin')
        else:
            messages.info(request,'Password doesn not match')
            print("password not matching")
    return render(request, 'flightbookapp/createacc.html')

def dashboard (request):
    return render(request,'flightbookapp/dashboard.html')

def admin (request):
    return render(request,'flightbookapp/adminlogin.html')

def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password,is_staff=True)
        if user is None or not(user.is_staff):
            messages.info(request,'invalid ')
            return redirect('adminlogin')
        else:
            login(request,user)
            return redirect('admindashboard')
            

    else:    
        return render(request,'flightbookapp/adminlogin.html')

def admindashboard(request):

    items = flight_details.objects.all()
    context = {'items':items}
    return render(request,'flightbookapp/admindashboard.html',context)

def addflight(request):
    if request.method == 'POST':
        fnumber = request.POST['fnumberi']
        airline = request.POST['airlinei']
        from_place = request.POST['fromi']
        to = request.POST['toi']
        depart = request.POST['departi']
        arrival = request.POST['arrivali']
        price = request.POST['pricei']
        capacity = request.POST['capacityi']
        vaccancy = request.POST['vaccancyi']
        flight = flight_details(flight_code=fnumber,airline=airline,source=from_place,destination=to,dep_date=depart,arrival_date=arrival,price=price,tot_seat_count=capacity,vacc_count=vaccancy)
        flight.save()
        print("created successfully")
        return  redirect('admindashboard')
    else:
        return render(request,'flightbookapp/addflight.html')

def deleteflight(request,fnumber):
    flight = flight_details.objects.get(flight_code=fnumber)
    flight.delete()
    return redirect(admindashboard)

def searchflight(request):
    if request.method == 'GET':
        query= request.GET.get('d')
        submitbutton= request.GET.get('submit')
        username = request.GET.get('username')
        if query is not None:
            lookups= Q(dep_date__icontains=query)
            results= flight_details.objects.filter(lookups)
            context={'results': results,
                     'submitbutton': submitbutton,
                     'username':username}
            return render(request, 'flightbookapp/searchres.html', context)

        else:
            return render(request, 'flightbookapp/login.html')
    else:
        return render(request, 'flightbookapp/dashboard.html')

def bookticket(request,fnumber):
    flight = flight_details.objects.get(flight_code=fnumber)
    context = {'flight':flight}
    return render(request,'flightbookapp/book.html',context)

def confirmbook(request,fnumber):
    if request.method == 'POST':
        username = request.POST.get('username')
        tot = request.POST.get('not')
        flight = flight_details.objects.get(flight_code=fnumber)
        vacc_count=int(flight.vacc_count)-int(tot)
        if(vacc_count<0):
            return HttpResponse("Such number of tickets is not")
        else:
            flight_details.objects.filter(flight_code=fnumber).update(vacc_count = vacc_count)
            book = Booking_det(username=username,flight_code=flight)
            book.save()
            return  redirect('dashboard')
    else:
        return HttpResponse(fnumber)
