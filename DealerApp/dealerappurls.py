from django.urls import path

from DealerApp import views

urlpatterns = [
path('dealerhome', views.dealerhome, name="dealerhome"),
path('viewrequestdealer', views.viewrequestdealer, name="viewrequestdealer"),
path('requesttoadmin_process', views.requesttoadmin_process, name="requesttoadmin_process"),
path('viewpayments', views.viewpayments, name="viewpayments"),
path('viewdelivery', views.viewdelivery, name="viewdelivery"),
path('deliverydetails/<requestmasterid>/', views.delivery_details, name='deliverydetails'),
path('dealerprofile', views.dealerprofile, name="dealerprofile"),
path('editdealerprofile/<dealerid>', views.editdealerprofile, name="editdealerprofile"),

]