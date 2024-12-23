from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('about/',views.About,name='about'),
    path('contact/',views.Book,name='contact'),
    path('menu/',views.Menu,name='menu'),
    # path('success',views.success,name='success'),
    # path('internshipdetails',views.internshipdetails,name='internshipdetails'),
]
