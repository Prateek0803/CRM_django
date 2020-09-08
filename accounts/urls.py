from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('products/',views.products,name="products"),
    path('customer/<str:pk>/',views.customer, name="customer"),
    path('create_order/',views.createOrder,name="create_order"),
    path('update_order/<str:key>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:key>/', views.deleteOrder, name="delete_order"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('logout/',views.logoutUser,name="logout")
]
