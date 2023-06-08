from django.urls import path
from shopapp import views

urlpatterns = [
    path('homepage1/',views.homepage1,name="homepage1"),
    path('categorypage/', views.categorypage, name="categorypage"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('categorydisplay/',views.categorydisplay,name="categorydisplay"),
    path('editcategory/<int:dataid>/',views.editcategory,name='editcategory'),
    path('updatecategory/<int:dataid>/',views.updatecategory,name='updatecategory'),
    path('categorydelete/<int:dataid>/',views.categorydelete,name='categorydelete'),
    path('addproductpage/',views.addproductpage,name='addproductpage'),
    path('saveproduct/',views.saveproduct,name='saveproduct'),
    path('displayproduct/',views.displayproduct,name='displayproduct'),
    path('editproduct/<int:dataid>/',views.editproduct,name='editproduct'),
    path('updateproduct/<int:dataid>/',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name='deleteproduct'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('additems/',views.additems,name='additems'),
    path('saveitems/',views.saveitems,name='saveitems'),
    path('displayitems/',views.displayitems,name='displayitems'),
    path('edititems/<dataid>/',views.edititems,name='edititems'),
    path('updateitem/<dataid>/',views.updateitem,name='updateitem'),
    path('deleteitem/<dataid>/',views.deleteitem,name='deleteitem'),

]