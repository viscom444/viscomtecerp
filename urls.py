"""crm9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crmapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('success/', views.retsuc,name='suc'),
    path('',views.homepage,name='homepage'),
    
    
    path('custcreate/',views.custcreate.as_view(),name='custcreate'),
    path('custdel/',views.custdel,name='custdel'),
    path('custdelsearch/',views.custdelsearch,name='custdelsearch'),
    path('custshowall/',views.custshowall,name='custshowall'),
    path('custsearch/',views.custsearch,name='custsearch'),
    path('custsearchform/',views.custsearchform,name='custsearchform'),
    path('custupdsearch/',views.custupdsearch,name='custupdsearch'),
    path('custupdshow/',views.custupdshow,name='custupdshow'),
    path('custupd/',views.custupd,name='custupd'),



    path('leadshowall/',views.leadshowall,name='leadshowall'),
    path('leadshowsearch/',views.leadshowsearch,name='leadshowsearch'),
    path('leadshowbyid/',views.leadshowbyid,name='leadshowbyid'),
    path('leadcreate/',views.leadcreate.as_view(),name='leadcreate'),
    path('leadupdsearch/',views.leadupdsearch,name='leadupdsearch'),
    path('leadupdshow/',views.leadupdshow,name='leadupdshow'),
    path('leaddelsearch/',views.leadupd,name='leaddelsearch'),
    path('leaddel/',views.leaddel,name='leaddel'),
    
    
]