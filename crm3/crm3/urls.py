"""crm3 URL Configuration

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
    path('succ', views.retsuc,name='succ'),
    path('',views.homepage,name='homepage'),
    
    path('custshow/<int:custid>/',views.show,name='custshow'),
    path(r'^custid/(?P<id>[0-9]+)/$',views.showtest,name='showtest'),
    path('custcreate/',views.custcreate.as_view(),name='custcreate'),
    path('custupd/<int:pk>/',views.custupd.as_view(),name='custupd'),
    path('custdel/<int:pk>/',views.custdel.as_view(),name='custdel'),
    path('custshow1/<int:pk>/',views.custshowrec),
    path('custsearch',views.custsearch),
    

    path('accshow/',views.accshow.as_view(),name='accshow'),
    path('acccreate/',views.acccreate.as_view(),name='acccreate'),
    path('accupd/<int:pk>/',views.accupd.as_view(),name='accupd'),
    path('accdel/<int:pk>/',views.accdel.as_view(),name='accdel'),

    path('leadshow/',views.leadshow.as_view(),name='leadshow'),
    path('leadcreate/',views.leadcreate.as_view(),name='leadcreate'),
    path('leadupd/<int:pk>/',views.leadupd.as_view(),name='leadupd'),
    path('leaddel/<int:pk>/',views.leaddel.as_view(),name='leaddel'),
    
    
    
]
