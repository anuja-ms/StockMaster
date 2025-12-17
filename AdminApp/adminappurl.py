from django.urls import path
from AdminApp import views
from AdminApp.views import ExportExcelMonthlyPurchase, ExportExcelMonthlySales

urlpatterns = [
    path('index', views.index, name="index"),
    path('district', views.district, name="district"),
    path('district_process', views.district_process, name="district_process"),
    path('viewdistrict', views.viewdistrict, name="viewdistrict"),
    path('deletedistrict/<districtid>', views.deletedistrict, name="deletedistrict"),
    path('editdistrict/<districtid>', views.editdistrict, name="editdistrict"),

    path('location',views.location,name="location"),
    path('location_process',views.location_process,name="location_process"),
    path('viewlocation',views.viewlocation,name="viewlocation"),
    path('filllocation',views.filllocation,name="filllocation"),
    path('deletelocation/<locationid>',views.deletelocation,name="deletelocation"),
    path('editlocation/<locationid>', views.editlocation, name="editlocation"),

    path('brand', views.brand, name="brand"),
    path('brand_process', views.brand_process, name="brand_process"),
    path('viewbrand', views.viewbrand, name="viewbrand"),
    path('deletebrand/<brandid>', views.deletebrand, name="deletebrand"),
    path('editbrand/<brandid>', views.editbrand, name="editbrand"),

    path('category',views.category,name="category"),
    path('category_process',views.category_process,name="category_process"),
    path('viewcategory',views.viewcategory,name="viewcategory"),
    path('deletecategory/<categoryid>',views.deletecategory,name="deletecategory"),
    path('editcategory/<categoryid>', views.editcategory, name="editcategory"),

    path('subcategory',views.subcategory,name="subcategory"),
    path('subcategory_process',views.subcategory_process,name="subcategory_process"),
    path('viewsubcategory',views.viewsubcategory,name="viewsubcategory"),
    path('fillsubcategory',views.fillsubcategory,name="fillsubcategory1"),
    path('editsubcategory/<subcategoryid>', views.editsubcategory, name="editsubcategory"),
    path('deletesubcategory/<subcategoryid>',views.deletesubcategory,name="deletesubcategory"),

    path('dealer', views.dealer, name="dealer"),
    path('dealer_process', views.dealer_process, name="dealer_process"),
    path('viewdealer', views.viewdealer, name="viewdealer"),
    path('filldealer', views.filldealer, name="filldealer"),
    path('editdealer/<dealerid>', views.editdealer, name="editdealer"),
    path('deletedealer/<dealerid>', views.deletedealer, name="deletedealer"),

    path('staff', views.staff, name="staff"),
    path('staff_process', views.staff_process, name="staff_process"),
    path('viewstaff', views.viewstaff, name="viewstaff"),
    path('fillstaff', views.fillstaff, name="fillstaff"),
    path('deletestaff/<staffid>', views.deletestaff, name="deletestaff"),
    path('editstaff/<staffid>', views.editstaff, name="editstaff"),

    path('product',views.product,name="product"),
    path('product_process',views.product_process,name="product_process"),
    path('viewproduct',views.viewproduct,name="viewproduct"),
    path('fillproduct',views.fillproduct,name="fillproduct"),
    path('deleteproduct/<productid>',views.deleteproduct,name="deleteproduct"),
    path('editproduct/<productid>', views.editproduct, name="editproduct"),

    path('stock', views.stock, name="stock"),
    path('stock_process', views.stock_process, name="stock_process"),
    path('viewstock', views.viewstock, name="viewstock"),
    path('fillstock', views.fillstock, name="fillstock"),
    path('deletestock/<stockid>', views.deletestock, name="deletestock"),
    path('editstock/<stockid>', views.editstock, name="editstock"),

    path('viewrequestdetails', views.viewrequestdetails, name="viewrequestdetails"),
    path('fillrequestdetails', views.fillrequestdetails, name="fillrequestdetails"),
    path('dealerrequest_process', views.dealerrequest_process, name="dealerrequest_process"),

    path('viewdealernotifiaction', views.viewdealernotification, name="viewdealernotification"),
    path('viewrequestmasterdetails/<requestmasterid>', views.viewrequestmasterdetails, name="viewrequestmasterdetails"),

    path('viewpurchasenotification', views.viewpurchasenotification, name="viewpurchasenotification"),
    path('viewbilling/<purchasemasterid>',views.viewbilling,name="viewbilling"),

    path('payment/<purchasemasterid>', views.payment, name="payment"),
    path('payment_process', views.payment_process, name="payment_process"),
    path('viewpayment', views.viewpayment, name="viewpayment"),
    path('piechartstockbasedproducts', views.piechartstockbasedproducts, name="piechartstockbasedproducts"),
    path('piechartbrandbasedproducts', views.piechartbrandbasedproducts, name="piechartbrandbasedproducts"),
    path('barchartsalesbasedproducts', views.barchartsalesbasedproducts, name="barchartsalesbasedproducts"),
    path('ExportExcelMonthlyPurchase', ExportExcelMonthlyPurchase.as_view(), name='ExportExcelMonthlyPurchase'),
    path('ExportExcelMonthlySales', ExportExcelMonthlySales.as_view(), name='ExportExcelMonthlySales'),
    path('allstaffrequest', views.allstaffrequest, name="allstaffrequest"),
    path('allstaffrequest_process', views.allstaffrequest_process, name="allstaffrequest_process"),
]