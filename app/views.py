"""
Definition of views.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import User, Area, Order,Feedback
from django.http import JsonResponse
from django.contrib import messages
from .models import User

def Home(request):
 
    return render(request, 'home.html')


def base(request):
 
    return render(request, 'base.html')


def feedback(request):
    return render(request, 'feedback.html')

def admin_user(request):
    all_users = User.objects.all()
    return render(request, 'admin_user.html', {'users': all_users})


def admin_area(request):
    all_areas = Area.objects.all()
    return render(request, 'admin_area.html', {'areas': all_areas})

def admin_order(request):
    all_orders = Order.objects.all()
    return render(request, 'admin_order.html', {'orders': all_orders})

def admin_feedback(request):
    all_feedbacks = Feedback.objects.all()
    return render(request, 'admin_feedback.html', {'feedbacks': all_feedbacks})




def booking(request):
    areas = Area.objects.all()  

    return render(request, 'booking.html', {'areas': areas})

def logout(request):
    request.session['email'] = ''
    return render(request, 'login.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        nickname = request.POST.get("nickname")

        try:
            user = User.objects.get(Email=email)
        except User.DoesNotExist:
            return JsonResponse({"message": "Email not registered"}, status=400)

        request.session['email'] = email

        if user.NickName != nickname:
            return JsonResponse({"message": "Incorrect nickname"}, status=400)

        if nickname == "user":

            return redirect('home')
        elif nickname == "administer":
            return redirect('admin_user')
    return JsonResponse({"message": "Wrong Log In"}, status=400)

def orders(request):

    orders = Order.objects.filter(Email=request.session['email'])

    return render(request, 'orders.html',{'orders':orders})

def profile(request):
    user = User.objects.get(Email=request.session['email'])

    return render(request, 'profile.html',{'user': user})

def register(request):

    return render(request, 'register.html')

def register_view(request):
     if request.method == "POST":
        email = request.POST.get("email") 
        password = request.POST.get("password")  
        nickname = request.POST.get("nickname")
        phone = request.POST.get("phone")

        if User.objects.filter(Email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')

        try:
            new_user = User(Email=email, Password=password, NickName=nickname, Phone=phone)
            new_user.save()

            return redirect('logout')
        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return redirect('register')

def profile_view(request):
    user = User.objects.get(Email=request.session['email'])
    print(vars(request.POST))
    if request.method == 'POST':

        user.NickName = request.POST.get('nickname')
        user.email = request.POST.get('email')
        user.Password = request.POST.get('password')
        user.Phone = request.POST.get('phone')
        user.money = request.POST.get('money')
        user.save()

        return redirect('profile_edit')

    return render(request, 'profile.html', {'user': user})

def feedback_upload(request):
    print(vars(request.POST))
    feedback= Feedback(text = request.POST.get('feedback'), time = datetime.now(), name = request.session['email'])
    feedback.save()
    return redirect('Orders')


def booking_now(request):
  if request.method == 'POST':
    Email = request.session['email']
    Order_Area = request.POST.get('area_name')
    Start_Time = request.POST.get('start_time')
    End_Time = request.POST.get('end_time')
    Payment = request.POST.get('payment')
    print(vars(request.POST))


    try:
        user = User.objects.get(Email=Email)
    except User.DoesNotExist:
        return JsonResponse({"message": "Email not registered"}, status=400)

    try:
        Area_book = Area.objects.get(Name=Order_Area, Start_Time=Start_Time, End_Time=End_Time)
    except Area.DoesNotExist:
        return JsonResponse({"message": "Area not registered"}, status=400)

    if Area_book.Order == False:
        Order_number = str(datetime.now()) + Email

        Order_here = Order(Order_Area=Order_Area, Order_number=Order_number, Payment=Payment,
                           Start_Time=Start_Time, End_Time=End_Time, Email=Email)
        Order_here.save()

        user.Money -= int(Payment)
        user.save()

        Area_book.Order = True
        Area_book.save()
        return redirect("home")
  return JsonResponse({"message": "Booking Failed"}, status=400)
