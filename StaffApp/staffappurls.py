from django.urls import path

from StaffApp import views

urlpatterns = [
path('staffhome', views.staffhome, name="staffhome"),
path('requestproduct',views.requestproduct,name="requestproduct"),
path('fillproducts',views.fillproducts,name="fillproducts"),
path('requestdetails_process',views.requestdetails_process,name="requestdetails_process"),

path('salesdetails', views.salesdetails, name="salesdetails"),
path('salesdetails_process', views.salesdetails_process, name="salesdetails_process"),
path('fillproductss', views.fillproductss, name="fillproductss"),
path('deletesalesdetails/<salesdetailsid>', views.deletesalesdetails, name="deletesalesdetails"),
path('salesmaster_process', views.salesmaster_process, name="salesmaster_process"),
path('purchasedetails', views.purchasedetails, name="purchasedetails"),
path('fillsubcategory/', views.fillsubcategory, name='fillsubcategory'),
path('fillproductsss/', views.fillproductsss, name='fillproductsss'),
path('get_product_details/', views.get_product_details, name='get_product_details'),
path('purchasedeatilsprocess', views.purchasedeatilsprocess, name="purchasedeatilsprocess"),
path('deletepurchasedetails/<purchasedetailsid>', views.deletepurchasedetails, name="deletepurchasedetails"),
path('purchasemaster_process', views.purchasemaster_process, name="purchasemaster_process"),
path('catsubview/<id>', views.catsubview, name='catsubview'),
path('subproductview/<subcategory_id>', views.subproductview, name='subproductview'),
path('staffprofile', views.staffprofile, name="staffprofile"),
path('editstaffprofile/<staffid>', views.editstaffprofile, name="editstaffprofile"),
path('logout/', views.logout, name='logout'),

]