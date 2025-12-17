from datetime import date
from decimal import Decimal
from django.db.models import F
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from AdminApp.models import Tbl_brand, Tbl_staff, Tbl_subcategory, Tbl_stock, Tbl_product, Tbl_dealer, Tbl_category
from StaffApp import views
from StaffApp.models import Tbl_requestmaster, Tbl_requestdetails, Tbl_purchasedetails, Tbl_purchasemaster, \
    Tbl_salesdetails, Tbl_salesmaster
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def staffhome(request):
    logid = request.session.get('loginId')
    if logid:
        cat=Tbl_category.objects.all()
        return render(request,'Staff/staffhome.html',{'cat':cat})
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def catsubview(request,id):
    logid = request.session.get('loginId')
    if logid:
        request.session['categoryid'] = id
        hos = Tbl_subcategory.objects.filter(categoryid=id)
        return render(request, "Staff/catsubview.html", {'cat': hos})
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def subproductview(request, subcategory_id):
    logid = request.session.get('loginId')
    if logid:
        """Fetch products based on the selected subcategory"""
        products = Tbl_product.objects.filter(subcategoryid=subcategory_id)
        return render(request, "Staff/subproductview.html", {'products': products})
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requestproduct(request):
    logid = request.session.get('loginId')
    if logid:
        brands=Tbl_brand.objects.all()
        sid=Tbl_staff.objects.get(loginid=request.session['loginId'])
        scid=Tbl_subcategory.objects.filter(categoryid=sid.categoryid)
        return render(request,'Staff/requestproduct.html',{'subcategory':scid,'brands':brands})
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillproducts(request):
    logid = request.session.get('loginId')
    if logid:
        sid = int(request.POST.get("sid"))
        bid = int(request.POST.get("bid"))
        products = Tbl_stock.objects.select_related('productid').filter(
            productid__subcategoryid__subcategoryid=sid,
            productid__brandid__brandid=bid,
            stock__lt=F('Reorderlevel')  # Correct way to compare stock with Reorderlevel
        ).values(
            'productid__productname',
            'productid__description',
            'productid__price',
            'productid__unit',
            'productid__image',
            'productid__brandid__brandname',
            'productid__productid',
            'stock',
            'Reorderlevel'
        )

        Tbl_requestmaster.objects.filter()
        return JsonResponse(list(products), safe=False)
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requestdetails_process(request):
    logid = request.session.get('loginId')
    if logid:
        if request.method == "POST":
            product_ids = request.POST.getlist("productid[]")  # Retrieves all selected product IDs
            for p in product_ids:
                staffid = Tbl_staff.objects.get(loginid=request.session['loginId'])
                productid = Tbl_product.objects.get(productid=p)
                rob = Tbl_requestdetails()
                rob.requestdate = date.today()
                rob.status = "Requested"
                rob.staffid = staffid
                rob.productid = productid
                rob.save()
            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Staff/requestproduct';</script>")
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def salesdetails(request):
    logid = request.session.get('loginId')
    if logid:
        brands = Tbl_brand.objects.all()
        sid = Tbl_staff.objects.get(loginid=request.session['loginId'])
        scid = Tbl_subcategory.objects.filter(categoryid=sid.categoryid)
        sales = Tbl_salesdetails.objects.filter(salesmasterid__isnull=True)
        return render(request, 'Staff/salesdetails.html', {'subcategory': scid, 'brands': brands, 'sales': sales})
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def salesdetails_process(request):
    logid = request.session.get('loginId')
    if logid:
        if request.method == "POST":
            sproductid = request.POST.get("productid")
            squantity = int(request.POST.get("quantity"))
            sproductamount = int(request.POST.get("productamount"))

            try:
                # Try to get the stock record for the chosen product
                stock = Tbl_stock.objects.get(productid=sproductid)

                # Check if there's enough stock available
                if stock.stock >= squantity:
                    # If there is enough stock, proceed with inserting the sales detail
                    sob = Tbl_salesdetails()
                    sob.quantity = squantity
                    sob.productamount = sproductamount
                    sob.productid = Tbl_product.objects.get(productid=sproductid)
                    sob.save()

                    # Update stock after sale
                    stock.stock -= squantity  # Decrease stock by the sold quantity
                    stock.save()

                    # Return success message and redirect
                    return HttpResponse(
                        "<script>alert('Successfully Inserted and stock updated!');window.location='/Stockmaster/Staff/salesdetails';</script>"
                    )
                else:
                    # If not enough stock is available, show an error message
                    return HttpResponse(
                        "<script>alert('Not enough stock available.');window.location='/Stockmaster/Staff/salesdetails';</script>"
                    )

            except Tbl_stock.DoesNotExist:
                # If the product is not found in the stock table, show a message
                return HttpResponse(
                    "<script>alert('Product not available in stock.');window.location='/Stockmaster/Staff/salesdetails';</script>"
                )
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillproductss(request):
    logid = request.session.get('loginId')
    if logid:
        sid = request.POST.get('sid')
        bid = request.POST.get('bid')
        products = Tbl_product.objects.filter(subcategoryid=sid, brandid=bid)

        product_data = []
        for product in products:
            product_data.append({
                'productid': product.productid,
                'productname': product.productname,
                'price': product.price,  # Include price here
            })

        return JsonResponse(product_data, safe=False)
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletesalesdetails(request, salesdetailsid):
    logid = request.session.get('loginId')
    if logid:
        # Get the sales detail entry to be deleted
        sob = Tbl_salesdetails.objects.get(salesdetailsid=salesdetailsid)

        # Get the related stock record for the product
        stock = Tbl_stock.objects.get(productid=sob.productid)

        # Increase the stock by the quantity from the deleted sales detail
        stock.stock += sob.quantity  # Add the sold quantity back to stock

        # Save the updated stock record
        stock.save()

        # Delete the sales detail
        sob.delete()

        # Return success message
        return HttpResponse(
            "<script>alert('Successfully Deleted and stock updated!');window.location='/Stockmaster/Staff/salesdetails'</script>")
    else:
        return HttpResponse(
            "<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def salesmaster_process(request):
    logid = request.session.get('loginId')
    if logid:
        if request.method == "POST":
            print(request.POST)

            # Get form data
            billingno = request.POST.get("billno")
            salesdate = request.POST.get("salesdate")
            grandtotal = request.POST.get("grandTotal")
            sid = Tbl_staff.objects.get(loginid=request.session['loginId'])

            # Convert grandTotal to Decimal
            try:
                grandtotal = Decimal(grandtotal)
            except (ValueError, TypeError):
                return HttpResponse(
                    "<script>alert('Invalid grand total value');window.location='/Stockmaster/Staff/salesdetails';</script>")

            # Create a new sales master record
            new_salesmaster = Tbl_salesmaster.objects.create(
                billingno=billingno,
                totalamount=grandtotal,
                salesdate=salesdate
            )

            # Insert new sales master ID into sales details table where salesmasterid is NULL
            updated_count = Tbl_salesdetails.objects.filter(
                salesmasterid__isnull=True,  # Select only NULL salesmasterid rows
                staffid__isnull=True  # Ensure correct staff association
            ).update(salesmasterid=new_salesmaster.salesmasterid, staffid=sid)

            # Success message
            return HttpResponse(
                "<script>alert('Successfully Inserted..');window.location='/Stockmaster/Staff/salesdetails'</script>")
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def purchasedetails(request):
    logid = request.session.get('loginId')
    if logid:
        cat = Tbl_category.objects.all()
        pro = Tbl_product.objects.all()
        dealer = Tbl_dealer.objects.all()
        purchase = Tbl_purchasedetails.objects.filter(purchasemasterid__isnull=True)
        return render(request, 'Staff/purchasedetails.html',{'dealer': dealer, 'pro': pro, 'cat': cat, 'purchase': purchase, 'dealer': dealer})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

# View to fetch subcategories based on category
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillsubcategory(request):
    logid = request.session.get('loginId')
    if logid:
        category_id = request.POST.get('cid')
        subcategories = Tbl_subcategory.objects.filter(categoryid=category_id)
        data = [{'subcategoryid': sc.subcategoryid, 'subcategoryname': sc.subcategoryname} for sc in subcategories]
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

# View to fetch products based on subcategory
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def fillproductsss(request):
    logid = request.session.get('loginId')
    if logid:
        subcategory_id = request.POST.get('sid')
        products = Tbl_product.objects.filter(subcategoryid=subcategory_id)
        data = [{'productid': p.productid, 'productname': p.productname} for p in products]
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

# View to fetch product details (price and stock)
# View to fetch product details (price and stock)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def get_product_details(request):
    logid=request.session.get('loginId')
    if logid:
        product_id = request.POST.get('pid')
        product = Tbl_product.objects.get(productid=product_id)
        data = {'price': product.price, 'dealerprice': product.dealerprice}
        return JsonResponse(data)
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def purchasedeatilsprocess(request):
    logid = request.session.get('loginId')
    if logid:
        if request.method == "POST":
            productid = request.POST.get("productid")
            quantity = int(request.POST.get("quantity"))  # Quantity should be an integer
            productamount = float(request.POST.get("productamount"))  # Change to float if it's a decimal

            # Save the purchasedetail
            pd = Tbl_purchasedetails()
            pd.quantity = quantity
            pd.productprice = productamount
            pd.productid = Tbl_product.objects.get(productid=productid)
            pd.save()

            # Now increase the stock based on the purchased quantity
            product = pd.productid  # Get the purchased product

            # Try to get the stock for the given product, if it exists
            try:
                stock = Tbl_stock.objects.get(productid=product)
                stock.stock += quantity  # Increase the stock by the purchased quantity
            except Tbl_stock.DoesNotExist:
                # If stock record doesn't exist, create a new stock record
                stock = Tbl_stock(productid=product, stock=quantity, Reorderlevel=0)

            stock.save()  # Save the updated/created stock record

            return HttpResponse(
                "<script>alert('Successfully Inserted');window.location='/Stockmaster/Staff/purchasedetails';</script>")
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletepurchasedetails(request, purchasedetailsid):
    logid=request.session.get('loginId')
    if logid:
        # Get the purchasedetail object to be deleted
        sob = Tbl_purchasedetails.objects.get(purchasedetailsid=purchasedetailsid)

        # Get the product associated with this purchase detail
        product = sob.productid

        # Get the current stock for the product
        try:
            stock = Tbl_stock.objects.get(productid=product)
            stock.stock -= sob.quantity  # Decrease the stock by the purchased quantity
            stock.save()  # Save the updated stock
        except Tbl_stock.DoesNotExist:
            # Handle the case if stock doesn't exist for the product
            pass  # You can add custom handling here, e.g., create stock if needed

        # Delete the purchasedetail record
        sob.delete()

        # Redirect with a success message
        return HttpResponse(
            "<script>alert('Successfully Deleted..');window.location='/Stockmaster/Staff/purchasedetails'</script>")
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def purchasemaster_process(request):
    logid=request.session.get('loginId')
    if logid:
        if request.method == "POST":
            print(request.POST)
            # Get form data
            billingno = request.POST.get("billno")
            purchasedate = request.POST.get("purchasedate")
            grandtotal = request.POST.get("grandTotal")
            dealers = request.POST.get("dealers")

            sid = Tbl_staff.objects.get(loginid=request.session['loginId'])

            # Convert grandTotal to Decimal
            try:
                grandtotal = Decimal(grandtotal)
            except (ValueError, TypeError):
                return HttpResponse("<script>alert('Invalid grand total value');window.location='/Stockmaster/Staff/purchasedetails';</script>")


            # Create a new sales master record
            new_purchasemaster = Tbl_purchasemaster.objects.create(
                billno=billingno,
                totalamount=grandtotal,
                dealerid=Tbl_dealer.objects.get(dealerid=dealers),
                purchasedate=purchasedate
            )

            # Insert new purchase master ID into purchase details table where purchasemasterid is NULL
            updated_count = Tbl_purchasedetails.objects.filter(
                purchasemasterid__isnull=True,  # Select only NULL purchasemasterid rows
                staffid__isnull=True  # Ensure correct staff association
            ).update(purchasemasterid=new_purchasemaster.purchasemasterid,staffid=sid)

            # Success message
            return HttpResponse("<script>alert('Successfully Inserted..');window.location='/Stockmaster/Staff/purchasedetails'</script>")
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def staffprofile(request):
    logid = request.session.get('loginId')
    if logid:
        staffid = Tbl_staff.objects.get(loginid=request.session['loginId']).staffid
        staff = Tbl_staff.objects.get(staffid=staffid)
        return render(request, "Staff/profile.html", {'staff': staff})
    else:
        return HttpResponse("<script>alert('Authenication Required Please login page');window.location='/login';</script>")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editstaffprofile(request,staffid):
    logid = request.session.get('loginId')
    if logid:
        if request.method=='POST':
            sname = request.POST.get("staffname")
            semail = request.POST.get("email")
            scontactno= request.POST.get("contactno")
            staff = Tbl_staff.objects.get(staffid=staffid)
            staff.staffname = sname
            staff.email = semail
            staff.contactno = scontactno
            staff.save()
            return staffprofile(request)
        staff = Tbl_staff.objects.get(staffid=staffid)
        return render(request,"Staff/editprofile.html",{'staff':staff})
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
