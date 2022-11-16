from django.conf.urls import url
from flightbookapp import views
from django.urls import path

urlpatterns = [
    #url(r'^$',views.index, name='index'),
    path('',views.userlogin,name='userlogin'),
    path('createacc',views.createacc,name='createacc'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('searchflight',views.searchflight,name='searchflight'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminlogin/admindashboard',views.admindashboard,name='admindashboard'),
    path('adminlogin/admindashboard/addflight',views.addflight,name='addflight'),
    path('adminlogin/deleteflight/<fnumber>',views.deleteflight,name='deleteflight'),
    path('bookticket/<fnumber>',views.bookticket,name='bookticket'),
    path('bookticket/<fnumber>/confirmbook',views.confirmbook,name='confirmbook'),
]