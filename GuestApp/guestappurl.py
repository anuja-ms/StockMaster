from django.urls import path
from GuestApp import views

urlpatterns = [
    path('',views.guesthome,name="guesthome"),
    path('login/', views.login, name="login"),
    path('login_process', views.login_process, name="login_process"),
    path('forgotpassword', views.forgotpassword, name="forgotpassword"),
]