from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('productlist/', views.ProductList.as_view(), name='productlist'),
    path('<slug>', views.ProductDetail.as_view(), name='productdetail'),
    path('addtocart/', views.AddToCart.as_view(), name='addtocart'),
    path('removetocart/', views.RemoveToCart.as_view(), name='RemoveToCart'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('search/', views.Search.as_view(), name='search'),
    path('pay/', views.Pay.as_view(), name='pay'),
    path('saveorder/', views.SaveOrder.as_view(), name='saveorder'),
    path('orderlist/', views.OrderList.as_view(), name='orderlist'),
    path('orderdetail/', views.OrderDetail.as_view(), name='orderdetail'),
]
