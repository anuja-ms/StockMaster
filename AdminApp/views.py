import smtplib
from datetime import date
from django.db.models import Sum
import xlwt
from email.message import EmailMessage
import smtplib

from django.views.generic import View
from django.db.models import F, Sum, Count
from django.shortcuts import render, get_object_or_404

from AdminApp.models import Tbl_district, Tbl_location, Tbl_brand, Tbl_subcategory, Tbl_category, Tbl_dealer, Tbl_staff, \
    Tbl_product, Tbl_stock
from django.http import HttpResponse,JsonResponse

from GuestApp.models import Tbl_login
from StaffApp import models
from StaffApp.models import Tbl_requestdetails, Tbl_requestmaster, Tbl_purchasemaster, Tbl_purchasedetails, Tbl_payment, \
    Tbl_salesdetails, Tbl_salesmaster
from django.utils.timezone import now
from datetime import timedelta

# Create your views here.
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Sum  # ✅ Correct import

def index(request):
    # Get the current month and year
    today = now().date()
    first_day = today.replace(day=1)
    last_day = today.replace(day=1) + timedelta(days=32)
    last_day = last_day.replace(day=1) - timedelta(days=1)

    # Monthly Sales Total Amount
    monthly_sales_total = Tbl_salesmaster.objects.filter(
        salesdate__range=[first_day, last_day]
    ).aggregate(total=Sum('totalamount'))['total'] or 0

    # Monthly Purchase Total Amount
    monthly_purchase_total = Tbl_purchasemaster.objects.filter(
        purchasedate__range=[first_day, last_day]
    ).aggregate(total=Sum('totalamount'))['total'] or 0

    # Supermarket Product Count
    product_count = Tbl_product.objects.count()

    # Product Stock Data for Pie Chart
    labels = []
    data = []

    queryset = Tbl_stock.objects.values('productid__productname').annotate(total_stock=Sum('stock'))
    for p in queryset:
        labels.append(p['productid__productname'])
        data.append(p['total_stock'])

    context = {
        'monthly_sales_total': monthly_sales_total,
        'monthly_purchase_total': monthly_purchase_total,
        'product_count': product_count,
        'labels': labels,
        'data': data,
    }

    return render(request, 'Admin/index.html', context)

def district(request):
    return render(request,'Admin/district.html')

def district_process(request):
    if request.method == "POST":
        dname=request.POST.get("districtname")
        dob = Tbl_district()
        dob.districtname = dname
        if Tbl_district.objects.filter(districtname=dname).exists():
            return HttpResponse("<script>alert('Already Exists..');window.location='/Stockmaster/Admin/district';</script>")
        else:
            dob.save()
            return HttpResponse("<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewdistrict';</script>")

def viewdistrict(request):
    district=Tbl_district.objects.all()
    return render(request,'Admin/viewdistrict.html',{'district':district})

def deletedistrict(request,districtid):
    dob = Tbl_district.objects.get(districtid=districtid)
    dob.delete()
    return HttpResponse("<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewdistrict'</script>")

def editdistrict(request,districtid):
    if request.method=='POST':
        dname=request.POST.get("txtdistrict")
        dis = Tbl_district.objects.get(districtid=districtid)
        dis.districtname = dname
        dis.save()
        return viewdistrict(request)
    dis = Tbl_district.objects.get(districtid=districtid)
    return render(request,"Admin/editdistrict.html",{'dis':dis})

def location(request):
    districts = Tbl_district.objects.all()  # select * from Tbl_district
    return render(request, 'Admin/location.html', {'districts': districts})


def location_process(request):
    if request.method == "POST":
        districtid = request.POST.get("districtid")
        lname = request.POST.get("locationname")
        lob = Tbl_location()
        lob.locationname = lname
        lob.districtid = Tbl_district.objects.get(districtid=districtid)
        if Tbl_location.objects.filter(locationname=lname, districtid=districtid).exists():
            return HttpResponse(
                "<script>alert('Already Exists..');window.location='/Stockmaster/Admin/location';</script>")
        else:
            lob.save()
            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewlocation';</script>")


def viewlocation(request):
    districts = Tbl_district.objects.all()
    return render(request, 'Admin/viewlocation.html', {'districts': districts})


def filllocation(request):
    did=int(request.POST.get("did"))
    location = Tbl_location.objects.filter(districtid=did).values()
    return JsonResponse(list(location), safe=False)


def deletelocation(request, locationid):
    lob = Tbl_location.objects.get(locationid=locationid)
    lob.delete()
    return HttpResponse("<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewlocation'</script>")

def editlocation(request,locationid):
    if request.method=='POST':
        lname=request.POST.get("txtlocation")
        loc = Tbl_location.objects.get(locationid=locationid)
        loc.locationname = lname
        loc.save()
        return viewlocation(request)
    loc = Tbl_location.objects.get(locationid=locationid)
    return render(request,"Admin/editlocation.html",{'loc':loc})

def brand(request):
    return render(request,'Admin/brand.html')

def brand_process(request):
    if request.method == "POST":
        bname=request.POST.get("brandname")
        bimage=request.FILES["brandimage"]
        bob = Tbl_brand()
        bob.brandname = bname
        bob.brandimage = bimage
        if Tbl_brand.objects.filter(brandname=bname).exists():
            return HttpResponse("<script>alert('Already Exists..');window.location='/Stockmaster/Admin/brand';</script>")
        else:
            bob.save()
            return HttpResponse("<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewbrand';</script>")

def editbrand(request,brandid):
    if request.method == 'POST':
        bname = request.POST.get("txtbrand")
        brand = Tbl_brand.objects.get(brandid=brandid)
        brand.brandname = bname

        # Check if the user uploaded a new image
        if len(request.FILES) != 0:
            brand.brandimage = request.FILES["cimage"]
        else:
            # No new image uploaded, keep the old image
            oldimage = request.POST.get("oldimage")
            brand.brandimage = oldimage

        brand.save()
        return HttpResponse("<script>alert('Successfully Updated..');window.location='/Stockmaster/Admin/viewbrand';</script>")
    else:
        brand = Tbl_brand.objects.get(brandid=brandid)
        return render(request,"Admin/editbrand.html",{'brand':brand})

def viewbrand(request):
    brand=Tbl_brand.objects.all()
    return render(request,'Admin/viewbrand.html',{'brand':brand})

def deletebrand(request,brandid):
    bob = Tbl_brand.objects.get(brandid=brandid)
    bob.delete()
    return HttpResponse("<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewbrand'</script>")


def category(request):
    return render(request, 'Admin/category.html')


def category_process(request):
    if request.method == "POST":
        cname = request.POST.get("categoryname")  # textboxname = music
        cimage = request.FILES["categoryimage"]  # filename = music.png
        cob = Tbl_category()
        cob.categoryname = cname  # cob.categoryname = filename in table = value(eg:cob.categoryname = music)
        cob.categoryimage = cimage
        if Tbl_category.objects.filter(categoryname=cname).exists():
            return HttpResponse(
                "<script>alert('Already Exists..');window.location='/Stockmaster/Admin/category';</script>")
        else:
            cob.save()
            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewcategory';</script>")


def viewcategory(request):
    category = Tbl_category.objects.all()
    return render(request, 'Admin/viewcategory.html', {'category': category})


def deletecategory(request, categoryid):
    cob = Tbl_category.objects.get(categoryid=categoryid)
    cob.delete()
    return HttpResponse(
        "<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewcategory'</script>")

def editcategory(request,categoryid):
    if request.method=='POST':
        cname=request.POST.get("categoryname")
        cimage=request.POST.get("categoryimage")
        cat = Tbl_category.objects.get(categoryid=categoryid)
        cat.categoryname = cname
        cat.categoryimage = cimage
        if 'cimage' in request.FILES:
            cat.categoryimage = request.FILES["cimage"]
        else:
            cat.categoryimage = request.POST.get("oldimage")

        cat.save()
        return viewcategory(request)
    cat = Tbl_category.objects.get(categoryid=categoryid)
    return render(request,"Admin/editcategory.html",{'cat':cat})


def subcategory(request):
    categorys = Tbl_category.objects.all()
    return render(request, 'Admin/subcategory.html', {'categorys': categorys})


def subcategory_process(request):
    if request.method == "POST":
        categoryid = request.POST.get("categoryid")
        scname = request.POST.get("subcategoryname")
        scimage = request.FILES["subcategoryimage"]
        scob = Tbl_subcategory()
        scob.subcategoryname = scname
        scob.image = scimage
        scob.categoryid = Tbl_category.objects.get(categoryid=categoryid)
        if Tbl_subcategory.objects.filter(subcategoryname=scname, categoryid=categoryid).exists():
            return HttpResponse(
                "<script>alert('Already Exists..');window.location='/Stockmaster/Admin/subcategory';</script>")
        else:
            scob.save()
            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewsubcategory';</script>")


def viewsubcategory(request):
    categorys = Tbl_category.objects.all()
    return render(request, 'Admin/viewsubcategory.html', {'categorys': categorys})


def fillsubcategory(request):
    cid=int(request.POST.get("cid"))
    subcategory = Tbl_subcategory.objects.filter(categoryid=cid).values()
    return JsonResponse(list(subcategory), safe=False)


def deletesubcategory(request, subcategoryid):
    scob = Tbl_subcategory.objects.get(subcategoryid=subcategoryid)
    scob.delete()
    return HttpResponse("<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewsubcategory'</script>")

def editsubcategory(request,subcategoryid):
    if request.method=='POST':
        scname=request.POST.get("subcategoryname")
        scimage=request.POST.get("image")
        scat = Tbl_subcategory.objects.get(subcategoryid=subcategoryid)
        scat.subcategoryname = scname
        scat.image = scimage
        if 'scimage' in request.FILES:
            scat.image = request.FILES["scimage"]
        else:
            scat.image = request.POST.get("oldimage")

        scat.save()
        return viewsubcategory(request)
    scat = Tbl_subcategory.objects.get(subcategoryid=subcategoryid)
    return render(request,"Admin/editsubcategory.html",{'scat':scat})



def dealer(request):
    district=Tbl_district.objects.all()
    return render(request,'Admin/dealer.html',{'district':district})

def dealer_process(request):
    if request.method == "POST":
        lob = Tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role="dealer"
        if Tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Already Exists..');window.location='/Stockmaster/Admin/viewdealer';</script>")
        else:
            lob.save()
            dob = Tbl_dealer()
            dob.dealername = request.POST.get("dealername")
            dob.email = request.POST.get("email")
            dob.contactno = request.POST.get("contactno")
            dob.locationid = Tbl_location.objects.get(locationid=request.POST.get("locationid"))
            dob.loginid = lob
            dob.save()

            userame = request.POST.get("username")
            password = request.POST.get("password")
            dealername = request.POST.get("dealername")
            Email = request.POST.get('email')  # to address
            msg = EmailMessage()
            msg.set_content(
                'Dear ' + dealername + ',\n\n'
                                        'Welcome to StockMaster! 🎉 We are pleased to have you as one of our valued product suppliers.\n\n'
                                        'Our supermarket relies on trusted dealers like you to ensure a seamless supply of quality products in bulk. Below are your login credentials to access the dealer portal:\n\n'
                                        '🔹 Username: ' + userame + '\n'
                                                                    '🔹 Password: ' + password + '\n\n'
                                                                                                'Through the dealer portal, you can manage your product listings, track orders, and stay updated on new purchase requests from our supermarket.\n\n'
                                                                                                'If you have any questions or require assistance, feel free to contact our support team.\n\n'
                                                                                                'Looking forward to a successful partnership!\n\n'
                                                                                                'Best regards,\n'
                                                                                                'StockMaster Team'
            )
            msg['Subject'] = "Welcome to Stock Master – Your Login Credentials"
            msg['from'] = 'ams816201@gmail.com'
            msg['To'] = {Email}
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('ams816201@gmail.com', 'ymat xotj kuiw oymj')
                smtp.send_message(msg)
            return HttpResponse("<script>alert('Successfully registered');window.location='/Stockmaster/Admin/viewdealer';</script>")

def viewdealer(request):
    district=Tbl_district.objects.all()
    return render(request,'Admin/viewdealer.html',{'district':district})

def filldealer(request):
        lid = int(request.POST.get("lid"))
        dealer= Tbl_dealer.objects.filter(locationid=lid).values()
        return JsonResponse(list(dealer), safe=False)

def deletedealer(request,dealerid):
    dob = Tbl_dealer.objects.get(dealerid=dealerid)
    dob.delete()
    return HttpResponse("<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewdealer'</script>")

def editdealer(request,dealerid):
    if request.method=='POST':
        dname=request.POST.get("dealername")
        dmail = request.POST.get("email")
        dcno = request.POST.get("contactno")
        dealer = Tbl_dealer.objects.get(dealerid=dealerid)
        dealer.dealername = dname
        dealer.email=dmail
        dealer.contactno=dcno
        dealer.save()
        return viewdealer(request)
    dealer = Tbl_dealer.objects.get(dealerid=dealerid)
    return render(request,"Admin/editdealer.html",{'dealer':dealer})


def staff(request):
    districts = Tbl_district.objects.all()
    categorys = Tbl_category.objects.all()
    return render(request, 'Admin/staff.html', {'districts': districts, 'categorys': categorys})


def staff_process(request):
    if request.method == "POST":
        lob = Tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "staff"
        if Tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse(
                "<script>alert('Already Exists..');window.location='/Stockmaster/Admin/viewstaff';</script>")
        else:
            lob.save()
            sob = Tbl_staff()
            sob.staffname = request.POST.get("staffname")
            sob.email = request.POST.get("email")
            sob.contactno = request.POST.get("contactno")
            sob.locationid = Tbl_location.objects.get(locationid=request.POST.get("locationid"))
            sob.categoryid = Tbl_category.objects.get(categoryid=request.POST.get("categoryid"))
            sob.loginid = lob
            sob.save()

            userame = request.POST.get("username")
            password = request.POST.get("password")
            staffname=request.POST.get("staffname")
            Email = request.POST.get('email')  # to address
            msg = EmailMessage()
            msg.set_content('Dear ' + staffname + ',\n\n' +
                            'Welcome to StockMaster! 🎉 We are excited to have you as part of our team.\n\n' +
                            'Below are your login credentials for accessing the staff portal:\n' +
                            '🔹 Username: ' + userame + '\n' +
                            '🔹 Password: ' + password + '\n\n' +
                            'Please keep these credentials secure and do not share them with anyone.\n\n' +
                            'Best regards,\n' +
                            'StockMaster Team')
            msg['Subject'] = "Welcome to Stock Master – Your Login Credentials"
            msg['from'] = 'ams816201@gmail.com'
            msg['To'] = {Email}
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('ams816201@gmail.com', 'ymat xotj kuiw oymj')
                smtp.send_message(msg)

            return HttpResponse(
                "<script>alert('Successfully registered');window.location='/Stockmaster/Admin/viewstaff';</script>")


def viewstaff(request):
    district = Tbl_district.objects.all()
    categorys = Tbl_category.objects.all()
    return render(request, 'Admin/viewstaff.html', {'district': district, 'categorys': categorys})


def fillstaff(request):
    lid = int(request.POST.get("lid"))
    staff = Tbl_staff.objects.filter(locationid=lid).values('staffname', 'email', 'contactno','categoryid__categoryname', 'staffid')
    return JsonResponse(list(staff), safe=False)


def deletestaff(request, staffid):
    sob = Tbl_staff.objects.get(staffid=staffid)
    sob.delete()
    return HttpResponse("<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewstaff'</script>")

def editstaff(request,staffid):
    if request.method=='POST':
        sname = request.POST.get("staffname")
        semail = request.POST.get("email")
        scontactno= request.POST.get("contactno")
        staff = Tbl_staff.objects.get(staffid=staffid)
        staff.staffname = sname
        staff.email = semail
        staff.contactno = scontactno
        staff.save()
        return viewstaff(request)
    staff = Tbl_staff.objects.get(staffid=staffid)
    return render(request,"Admin/editstaff.html",{'staff':staff})


def product(request):
    categorys = Tbl_category.objects.all()
    brands = Tbl_brand.objects.all()
    return render(request, 'Admin/product.html', {'categorys': categorys, 'brands': brands})


def product_process(request):
    if request.method == "POST":
        brandid = request.POST.get("brandid")
        subcategoryid = request.POST.get("subcategoryid")
        pname = request.POST.get("productname")
        pdescription = request.POST.get("description")
        pdealerprice = request.POST.get("dealerprice")
        pprice = request.POST.get("price")
        punit = request.POST.get("unit")
        pimage = request.FILES["image"]
        pob = Tbl_product()
        pob.productname = pname
        pob.description = pdescription
        pob.dealerprice = pdealerprice
        pob.price = pprice
        pob.unit = punit
        pob.image = pimage
        pob.brandid = Tbl_brand.objects.get(brandid=brandid)
        pob.subcategoryid = Tbl_subcategory.objects.get(subcategoryid=request.POST.get("subcategoryid"))
        if Tbl_product.objects.filter(productname=pname, brandid=brandid, subcategoryid=subcategoryid).exists():
            return HttpResponse(
                "<script>alert('Already Exists..');window.location='/Stockmaster/Admin/product';</script>")
        else:
            pob.save()
            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewproduct';</script>")


def viewproduct(request):
    categorys = Tbl_category.objects.all()
    brands = Tbl_brand.objects.all()
    return render(request, 'Admin/viewproduct.html', {'categorys': categorys, 'brands': brands})


def fillproduct(request):
    sid = int(request.POST.get("sid"))
    products = Tbl_product.objects.filter(subcategoryid=sid).values('productname', 'description', 'price', 'unit','image', 'brandid__brandname', 'productid','dealerprice')
    return JsonResponse(list(products), safe=False)


def deleteproduct(request, productid):
    pob = Tbl_product.objects.get(productid=productid)
    pob.delete()
    return HttpResponse("<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewproduct'</script>")

def editproduct(request,productid):
    if request.method=='POST':
        pname=request.POST.get("productname")
        pdescription=request.POST.get("description")
        pdealerprice=request.POST.get("dealerprice")
        pprice=request.POST.get("price")
        punit=request.POST.get("unit")
        pimage=request.POST.get("image")
        pro = Tbl_product.objects.get(productid=productid)
        pro.productname = pname
        pro.description = pdescription
        pro.dealerprice = pdealerprice
        pro.price = pprice
        pro.unit = punit
        pro.image = pimage
        if 'pimage' in request.FILES:
            pro.image = request.FILES["pimage"]
        else:
            pro.image = request.POST.get("oldimage")

        pro.save()
        return viewproduct(request)
    pro = Tbl_product.objects.get(productid=productid)
    return render(request,"Admin/editproduct.html",{'pro':pro})



def stock(request):
    products = Tbl_product.objects.all()
    return render(request, 'Admin/stock.html', {'products': products})


def stock_process(request):
    if request.method == "POST":
        productid = request.POST.get("productid")
        stocks = request.POST.get("stock")
        reorderlevel = request.POST.get("Reorderlevel")
        sob = Tbl_stock()
        sob.stock = stocks
        sob.Reorderlevel = reorderlevel
        sob.productid = Tbl_product.objects.get(productid=productid)
        if Tbl_stock.objects.filter(stock=stocks, productid=productid).exists():
            return HttpResponse(
                "<script>alert('Already Exists..');window.location='/Stockmaster/Admin/stock';</script>")
        else:
            sob.save()
            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewstock';</script>")


def viewstock(request):
    categorys = Tbl_category.objects.all()
    products = Tbl_product.objects.all()
    return render(request, 'Admin/viewstock.html', {'categorys': categorys, 'products': products})


def fillstock(request):
    pid = int(request.POST.get("pid"))
    stocks = Tbl_stock.objects.filter(productid=pid).values('stock', 'Reorderlevel', 'stockid')
    return JsonResponse(list(stocks), safe=False)


def deletestock(request, stockid):
    sob = Tbl_stock.objects.get(stockid=stockid)
    sob.delete()
    return HttpResponse(
        "<script>alert('Successfully Deleted..');window.location='/Stockmaster/Admin/viewstock'</script>")

def editstock(request,stockid):
    if request.method=='POST':
        stock=request.POST.get("stock")
        reorderlevel=request.POST.get("Reorderlevel")
        stoc = Tbl_stock.objects.get(stockid=stockid)
        stoc.stock = stock
        stoc.Reorderlevel = reorderlevel
        stoc.save()
        return viewstock(request)
    stoc = Tbl_stock.objects.get(stockid=stockid)
    return render(request,"Admin/editstock.html",{'stoc':stoc})

def viewrequestdetails(request):
    staffs=Tbl_staff.objects.all()
    dealers=Tbl_dealer.objects.all()
    return render(request,'Admin/viewrequestdetails.html',{'staffs':staffs,'dealers':dealers})

def fillrequestdetails(request):
    sid=int(request.POST.get("sid"))
    requestdetails= Tbl_requestdetails.objects.filter(staffid=sid,status='Requested').select_related('productid').filter(productid__tbl_stock__productid=F('productid')).values(
            'productid__productname',
            'productid__productid',
            'productid__price',
            'productid__dealerprice',
            'requestdate',
            'productid__tbl_stock__stock',  # Fetch stock from Tbl_stock
            'productid__tbl_stock__Reorderlevel',  # Fetch Reorderlevel from Tbl_stock
            'staffid__categoryid__categoryname',
            'quantity',
            'status',
            'requestmasterid__totalamount'
        )
    return JsonResponse(list(requestdetails), safe=False)


def dealerrequest_process(request):
    if request.method == "POST":
        # Retrieve POST data
        productids = request.POST.getlist("productid[]")  # List of product IDs
        quantity_list = request.POST.getlist("qty[]")  # List of quantities for the products
        price_list = request.POST.getlist("amount[]")  # List of prices for the products
        remark = request.POST.get("remark")  # Remark input field
        dealerid = request.POST.get("dealerid")  # Dealer ID
        totalamount = request.POST.get("totalamount")  # Grand total for the request
        staffid = request.POST.get("staffid")
        # return  HttpResponse(dealerid)
        # Get the dealer object
        dealer = Tbl_dealer.objects.get(dealerid=dealerid)

        # Create a Tbl_requestmaster entry
        rmob = Tbl_requestmaster()
        rmob.totalamount = totalamount  # Set the grand total
        rmob.dealerid = dealer  # Associate the dealer
        rmob.status = "Requested To dealer"  # Set the status to "Requested"
        rmob.save()  # Save the Tbl_requestmaster object

        for i, product_id in enumerate(productids):
            # Get the correct Tbl_requestdetails object based on productid and staffid
            rob = Tbl_requestdetails.objects.get(
                productid__productid=product_id,
                staffid__staffid=staffid,
                requestmasterid__isnull=True  # Ensure it hasn't been assigned to a requestmaster yet
            )

            # Update the Tbl_requestdetails fields
            rob.quantity = quantity_list[i]
            rob.price = price_list[i]
            rob.remark = remark
            rob.status = "Request to Dealer"
            rob.requestmasterid = rmob  # Assign the newly created requestmaster
            rob.requestdate = date.today()
            rob.save()

            # Redirect back to the admin view page with a success message
        return HttpResponse(
            "<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewrequestdetails';</script>")

    else:
        return HttpResponse(
            "<script>alert('Invalid request method.');window.location='/Stockmaster/Admin/viewrequestdetails';</script>")

def viewdealernotification(request):
    result=Tbl_requestmaster.objects.filter(status='Completed',deliverydate__gte=date.today())
    return render(request,'Admin/viewdealernotification.html',{'result':result})

def viewrequestmasterdetails(request,requestmasterid):
    result=Tbl_requestdetails.objects.filter(requestmasterid=requestmasterid)
    requestmaster=Tbl_requestmaster.objects.get(requestmasterid=requestmasterid)
    grandtotal=Tbl_requestdetails.objects.filter(requestmasterid=requestmasterid).aggregate(Sum('price'))['price__sum']
    return render(request,'Admin/viewrequestmasterdetails.html',{'result':result,'requestmaster':requestmaster,'grandtotal':grandtotal})

def viewpurchasenotification(request):
    purchase=Tbl_purchasemaster.objects.all()
    return render(request,'Admin/purchasenotification.html',{'purchase':purchase})

def viewbilling(request,purchasemasterid):
    purchase=Tbl_purchasedetails.objects.filter(purchasemasterid=purchasemasterid)
    purchasemaster=Tbl_purchasemaster.objects.get(purchasemasterid=purchasemasterid)
    grandtotal=Tbl_purchasemaster.objects.filter(purchasemasterid=purchasemasterid).aggregate(Sum('totalamount'))['totalamount__sum']
    return render(request,'Admin/viewbilling.html',{'purchase':purchase,'purchasemaster':purchasemaster,'grandtotal':grandtotal})


def payment(request, purchasemasterid):
    purchasemaster = Tbl_purchasemaster.objects.get(purchasemasterid=purchasemasterid)
    return render(request, 'Admin/payment.html', {'purchasemaster': purchasemaster})


def payment_process(request):
    if request.method == "POST":
        purchasemasterid = request.POST.get("purchasemasterid")
        amount = request.POST.get("amount")
        pay = Tbl_payment()
        pay.Amount = amount
        pay.date = date.today()
        pay.status = "Paid"
        pay.purchasemasterid = Tbl_purchasemaster.objects.get(purchasemasterid=purchasemasterid)
        if Tbl_payment.objects.filter(purchasemasterid=purchasemasterid).exists():
            return HttpResponse(
                "<script>alert('Already Exists..');window.location='/Stockmaster/Admin/viewpayment';</script>")
        else:
            pay.save()
            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/viewpayment';</script>")

def viewpayment(request):
    payment=Tbl_payment.objects.all()
    return render(request,'Admin/viewpayment.html',{'payment':payment})

def piechartstockbasedproducts(request):
    labels = []
    data = []

    queryset = Tbl_stock.objects.values('productid__productname').annotate(total_stock=Sum('stock'))
    for p in queryset:
        labels.append(p['productid__productname'])  # Product ID
        data.append(p['total_stock'])

    return render(request, 'Admin/piechartstockbasedproducts.html', {
        'labels': labels,
        'data': data
    })

def piechartbrandbasedproducts(request):
    labels = []
    data = []

    queryset = Tbl_product.objects.values('brandid__brandname').annotate(total_product=Count('productid'))
    for b in queryset:
        labels.append(b['brandid__brandname'])  # Product ID
        data.append(b['total_product'])

    return render(request, 'Admin/piechartbrandbasedproducts.html', {
        'labels': labels,
        'data': data
    })

def barchartsalesbasedproducts(request):
    labels = []
    data = []

    queryset = Tbl_salesdetails.objects.values('productid__productname').annotate(total_product=Count('productid'))
    for p in queryset:
        labels.append(p['productid__productname'])  # Brand Name
        data.append(p['total_product'])  # Total Products

    return render(request, 'Admin/barchartsalesbasedproducts.html', {
        'labels': labels,
        'data': data
    })

class ExportExcelMonthlyPurchase(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="monthlypurchase.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Product Name', 'Purchase Date', 'Product Price', 'Quantity' , 'Totalamount', 'Bill No','Dealer Name']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        queryset = Tbl_purchasedetails.objects.select_related('purchasemasterid', 'productid').values_list('productid__productname', 'purchasemasterid__purchasedate', 'productprice','quantity','purchasemasterid__totalamount', 'purchasemasterid__billno','purchasemasterid__dealerid__dealername')
        # return HttpResponse(queryset)
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

class ExportExcelMonthlySales(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="monthlysales.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')

        # Define the column headings
        row_num = 0
        columns = ['Product Name', 'Sales date', 'Quantity', 'Product Price' , 'Totalamount', 'Billing No']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Query the data from your model, and write it to the worksheet
        queryset = Tbl_salesdetails.objects.select_related('salesmasterid', 'productid').values_list('productid__productname', 'salesmasterid__salesdate', 'quantity','productamount','salesmasterid__totalamount', 'salesmasterid__billingno')
        # return HttpResponse(queryset)
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

def allstaffrequest(request):
    req = Tbl_requestdetails.objects.filter(status="Requested")
    dealers = Tbl_dealer.objects.all()

    # Create a dictionary to store stock details for each product
    stock_details = {stock.productid: stock for stock in Tbl_stock.objects.all()}

    # Attach stock and reorder level details to each request object
    for r in req:
        stock_entry = stock_details.get(r.productid)  # Get stock entry if available
        r.stock = stock_entry.stock if stock_entry else 0
        r.reorderlevel = stock_entry.Reorderlevel if stock_entry else 0

    return render(request, 'Admin/allstaffrequest.html', {'req': req, 'dealers': dealers})


def allstaffrequest_process(request):
    if request.method == "POST":
        try:
            # Retrieve POST data
            productids = request.POST.getlist("productid[]")
            quantity_list = request.POST.getlist("quantity[]")
            price_list = request.POST.getlist("totalamount[]")
            remark = request.POST.get("remark", "")
            dealerid = request.POST.get("dealerid")

            if not dealerid:
                return HttpResponse(
                    "<script>alert('Dealer ID missing.');window.location='/Stockmaster/Admin/viewrequestdetails';</script>")

            dealer = get_object_or_404(Tbl_dealer, dealerid=dealerid)

            # Calculate total amount from price list
            total_amount = sum(float(price) for price in price_list if price)

            # Create a new request master record
            rmob = Tbl_requestmaster.objects.create(
                totalamount=total_amount,
                dealerid=dealer,
                status="Requested To Dealer"
            )

            for i, product_id in enumerate(productids):
                product = get_object_or_404(Tbl_product, productid=product_id)
                quantity = int(quantity_list[i]) if quantity_list[i] else 0
                price = float(price_list[i]) if price_list[i] else 0

                # Fetch existing request details where `requestmasterid` is NULL
                request_details = Tbl_requestdetails.objects.filter(
                    productid=product, requestmasterid__isnull=True
                ).first()  # Get the first available record

                if request_details:
                    # Update the existing record
                    request_details.quantity = quantity
                    request_details.price = price
                    request_details.remark = remark
                    request_details.status = "Request to Dealer"
                    request_details.requestmasterid = rmob
                    request_details.requestdate = date.today()
                    request_details.save()
                else:
                    # If no existing request details found, create a new one
                    Tbl_requestdetails.objects.create(
                        productid=product,
                        staffid=None,  # Set staffid to NULL
                        requestdate=date.today(),
                        remark=remark,
                        price=price,
                        status="Request to Dealer",
                        requestmasterid=rmob,
                        dealerquantity=quantity
                    )

            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Admin/allstaffrequest';</script>")

        except Exception as e:
            return HttpResponse(
                f"<script>alert('Error: {str(e)}');window.location='/Stockmaster/Admin/allstaffrequest';</script>")

    return HttpResponse(
        "<script>alert('Invalid request method.');window.location='/Stockmaster/Admin/allstaffrequest';</script>")
