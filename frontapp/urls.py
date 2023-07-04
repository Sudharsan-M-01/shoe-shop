from django.urls import path
from frontapp import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('product/<itemcat>/',views.product,name="product"),
    path('typess/<itemcat>/',views.typess,name="typess"),
    path('single/<dataid>/',views.single,name="single"),
    path('items/<itemcat>/',views.items,name="items"),
    path('deletecart/<dataid>/',views.deletecart,name="deletecart"),
    path('cart/',views.cart,name="cart"),
    path('savecartt/', views.savecartt, name="savecartt"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('checkout/',views.checkout,name="checkout"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('profile/',views.profile,name="profile"),
    path('usersavedata/',views.usersavedata,name="usersavedata"),
    path('userloginpage/',views.userloginpage,name="userloginpage"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('savecheckout/',views.savecheckout,name="savecheckout"),
    path('allpro/',views.allpro,name="allpro"),
]