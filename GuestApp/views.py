import random
import smtplib
import string
from email.message import EmailMessage

from django.http import HttpResponse
from django.shortcuts import render,redirect
from GuestApp.models import Tbl_login
from AdminApp.models import Tbl_staff, Tbl_dealer


# Create your views here.

def guesthome(request):
    return render(request,'Guest/guesthome.html')

def login(request):
    return render(request,'Guest/login.html')

def login_process(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        if Tbl_login.objects.filter(username=username,password=password).exists():
            logindata = Tbl_login.objects.get(username=username,password=password)
            request.session['loginId'] = logindata.loginid
            role = logindata.role
            if role == "Admin":
                return redirect('/Stockmaster/Admin/index')
            elif role == "staff":
                return redirect('/Stockmaster/Staff/staffhome')
            elif role == "dealer":
                return redirect('/Stockmaster/Dealer/dealerhome')
        else:
            context = {"error": "Incorrect username or password"}
            return render(request, "Guest/login.html", context)


def forgotpassword(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")

        # Check if user exists in customer or company tables
        if Tbl_staff.objects.filter(loginid__username=uname).exists():
            user = Tbl_staff.objects.get(loginid__username=uname)
            email = user.email
            name = user.staffname
        elif Tbl_dealer.objects.filter(loginid__username=uname).exists():
            user = Tbl_dealer.objects.get(loginid__username=uname)
            email = user.email
            name = user.dealername
        else:
            return HttpResponse(
                "<script>alert('No user found with this username.');window.location='/Stockmaster/Guest/login/';</script>")

        # Generate a new password
        characters = string.ascii_letters + string.digits
        new_password = ''.join(random.choice(characters) for _ in range(8))

        # Update the password in the database
        login_instance = Tbl_login.objects.get(username=uname)
        login_instance.password = new_password  # Ideally, hash this password!
        login_instance.save()

        # Send email with the new password
        msg = EmailMessage()
        msg.set_content(f'Dear  {name}, As per your request, we have generated a new temporary password for your account.Your new password to log in is: {new_password}')
        msg['Subject'] = "Password Reset Request"
        msg['From'] = 'ams816201@gmail.com'
        msg['To'] = email

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('ams816201@gmail.com', 'ymat xotj kuiw oymj')  # Ensure this is an App Password
                smtp.send_message(msg)
            return HttpResponse(
                "<script>alert('Login with the new password sent to your email.');window.location='/login/';</script>")
        except Exception as e:
            return HttpResponse(
                f"<script>alert('Email sending failed: {e}');window.location='/login/';</script>")

    return render(request, "Guest/forgot.html")
