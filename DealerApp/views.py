from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect

from AdminApp.models import Tbl_dealer
from StaffApp.models import Tbl_requestdetails, Tbl_requestmaster, Tbl_payment
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dealerhome(request):
    logid = request.session.get('loginId')
    if logid:
        did=Tbl_dealer.objects.get(loginid=request.session['loginId'])
        return render(request,'Dealer/dealerhome.html',{'dealer':did})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewrequestdealer(request):
    logid = request.session.get('loginId')
    if logid:
        requestdetails = Tbl_requestdetails.objects.filter(status="Request to Dealer")
        return render(request, 'Dealer/viewrequestdealer.html', {'requestdetails': requestdetails})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requesttoadmin_process(request):
    logid = request.session.get('loginId')
    if logid:
        if request.method == "POST":
            requestids = request.POST.getlist("requestid")  # List of product IDs
            dealerquantity = request.POST.getlist("dealerquantity")  # List of quantities for the products
            price = request.POST.getlist("totalamount")  # List of prices for the products
            deliverydate = request.POST.get("required_date")
            # totalamount = request.POST.get("grand_total")  # Grand total for the request

            # rmob = Tbl_requestmaster()
            # rmob.deliverydate = deliverydate
            # rmob.dealerid = Tbl_dealer.objects.get(loginid=request.session['loginId'])
            # rmob.totalamount = totalamount
            # rmob.status = "Completed"  # Set the status to "Requested"
            # rmob.save()  # Save the Tbl_requestmaster object

            for i, requestid in enumerate(requestids):
                rob = Tbl_requestdetails.objects.get(
                    requestid=requestid
                )
                # Get the corresponding Tbl_requestdetails record
                rob.dealerquantity = dealerquantity[i]
                rob.price = price[i]
                rob.status = "Completed"
                rob.save()

            result = Tbl_requestdetails.objects.filter(requestid__in=requestids).values('requestmasterid').annotate(
                total_amount_sum=Sum('price')).distinct()
            for res in result:
                requestmasterid = res['requestmasterid']
                total_amount_sum = res['total_amount_sum']
                rmob = Tbl_requestmaster.objects.get(requestmasterid=requestmasterid)
                rmob.deliverydate = deliverydate
                rmob.status = "Completed"
                rmob.totalamount = total_amount_sum
                rmob.save()
            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Dealer/viewrequestdealer';</script>")

        else:
            return HttpResponse(
                "<script>alert('Invalid request method.');window.location='/Stockmaster/Dealer/viewrequestdealer';</script>")
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewpayments(request):
    logid = request.session.get('loginId')
    if logid:
        did=Tbl_dealer.objects.get(loginid=request.session['loginId'])
        payments=Tbl_payment.objects.filter(purchasemasterid__dealerid=did)
        return render(request,'Dealer/viewpaymentdetails.html',{'payments':payments})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewdelivery(request):
    logid = request.session.get('loginId')
    if logid:
        did=Tbl_dealer.objects.get(loginid=request.session['loginId'])
        delivery=Tbl_requestmaster.objects.filter(dealerid=did)
        return render(request,'Dealer/viewdelivery.html',{'delivery':delivery})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewmoredelivery(request,requestid):
    logid = request.session.get('loginId')
    if logid:
        result=Tbl_requestdetails.objects.get(requestid=requestid)
        return render(request,'Dealer/viewmoredelivery.html',{'result':result})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delivery_details(request,requestmasterid):
    logid = request.session.get('loginId')
    if logid:
        delivery_master = Tbl_requestmaster.objects.get(requestmasterid=requestmasterid)
        delivered_items = Tbl_requestdetails.objects.filter(requestmasterid=delivery_master)

        return render(request, 'Dealer/viewmoredelivery.html', {
            'delivery_master': delivery_master,
            'delivered_items': delivered_items
        })
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dealerprofile(request):
    logid = request.session.get('loginId')
    if logid:
        dealerid = Tbl_dealer.objects.get(loginid=request.session['loginId']).dealerid
        dealer = Tbl_dealer.objects.get(dealerid=dealerid)
        return render(request, "dealer/profile.html", {'dealer': dealer})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editdealerprofile(request,dealerid):
    logid=request.session.get('loginId')
    if logid:
        if request.method=='POST':
            dname = request.POST.get("dealername")
            demail = request.POST.get("email")
            dcontactno= request.POST.get("contactno")
            dealer = Tbl_dealer.objects.get(dealerid=dealerid)
            dealer.dealername = dname
            dealer.email = demail
            dealer.contactno = dcontactno
            dealer.save()
            return dealerprofile(request)
        dealer = Tbl_dealer.objects.get(dealerid=dealerid)
        return render(request,"Dealer/editprofile.html",{'dealer':dealer})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    logid=request.session.get('loginId')
    if logid:
        request.session.clear()
        return redirect('/')
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")