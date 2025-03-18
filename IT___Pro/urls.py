"""
Definition of urls for IT___Pro.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import admin_user

urlpatterns = [
    path('', views.logout),
    path('Home/', views.Home,name = "home"),
    path('booking/', views.booking,name = "Booking"),
    path('login/', views.logout,name = "logout"),
    path('log_in/',views.login_view,name="login"),
    path('orders/', views.orders,name = "Orders"),
    path('profile/', views.profile,name = "profile_edit"),
    path('profile_view/', views.profile_view,name = "Profile"),
    path('register/', views.register,name ="register"),
    path('register_in/',views.register_view,name="register_in"),
    path('feedback/', views.feedback,name = "feedback"),
    path('admin_user/', views.admin_user,name = "admin_user"),
    path('admin_area/', views.admin_area, name="admin_area"),
    path('admin_order/', views.admin_order, name="admin_order"),
    path('admin_feedback/', views.admin_feedback, name="admin_feedback"),
    path('feedback_upload/',views.feedback_upload, name="feedback_upload"),
    path('booking_now/',views.booking_now, name="booking_now"),


]
