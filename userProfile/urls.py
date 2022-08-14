from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('singup/', views.SingUp.as_view(), name='singup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('update/', views.Update.as_view(), name='update'),
]
