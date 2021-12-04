from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from crmapp.models import crm3cust,crm3lead
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse


class custcreate(CreateView):
    model = crm3cust
    template_name = 'custcreate.html'
    fields = ['custid','custfname','custlname','custphone','custemail','custcompany','custbillingstreet','custbillingcity',
    'custbillingstate','custbillingcountry','custbillingpinzip','custshippingstreet','custshippingcity',
    'custshippingstate','custshippingcountry','custshippingpinzip']
    success_url=reverse_lazy('suc')

def custshowall(request):
    customer=crm3cust.objects.all()
    return render(request,"custshow.html",{'cus':customer})


def custsearch(request):
    custid=request.POST.get('custsearch')
    customer=crm3cust.objects.filter(custid=custid)
    return render(request,"custshow.html",{'cus':customer})

def custsearchform(request):
     return render(request,'custsearch.html')

def custupd(request):
    custid=request.POST.get('custid')
    customerupd=crm3cust.objects.get(custid=custid)
    customerupd.custfname=request.POST.get('custfname')
    customerupd.custlname=request.POST.get('custlname')
    customerupd.custphone=request.POST.get('custphone')
    customerupd.custemail=request.POST.get('custemail')
    customerupd.custcompany=request.POST.get('custcompany')
    customerupd.save()
    return render(request,"suc.html")
    
def custupdshow(request):
    custid=request.POST.get('custupdsearch')
    customer=crm3cust.objects.filter(custid=custid)
    return render(request,"custupd.html",{'cus':customer})
    
def custupdsearch(request):
    return render(request,'custupdsearch.html')

def custdelsearch(request):
    return render(request,'custdelsearch.html')

def custdel(request):
    custid=request.POST.get('custdelsearch')
    customer=crm3cust.objects.filter(custid=custid)
    customer.delete()
    return render(request,"suc.html")

class leadcreate(CreateView):
    model=crm3lead
    fields = ['leadid','leadfname','leadlname','leadphone','leademail','leadcompany','leadbillingstreet',
    'leadbillingcity','leadbillingstate','leadbillingcountry','leadbillingpinzip','leadshippingstreet',
    'leadshippingcity','leadshippingstate','leadshippingcountry','leadshippingpinzip']
    template_name='leadcreate.html'
    success_url=reverse_lazy('suc')

def leadshowall(request):
    leads=crm3lead.objects.all()
    return render(request,"leadshow.html",{'leads':leads})

def leadshowsearch(request):
    return render(request,"leadsearch.html")

def leadshowbyid(request):
    leadid=request.POST.get('leadsearch')
    leads=crm3lead.objects.filter(leadid=leadid)
    return render(request,"leadshow.html",{'leads':leads})    

def leadupd(request):
    leads=request.POST.get('leadid')
    leadupd=crm3lead.objects.filter(leadid=leadid)
    leadupd.leadfname=request.POST.get('leadfname')
    leadupd.leadlname=request.POST.get('leadlname')
    leadupd.leadphone=request.POST.get('leadphone')
    leadupd.leademail=request.POST.get('leademail')
    leadupd.leadcompany=request.POST.get('leadcompany')
    leadupd.save()
    return render(request,"suc.html")
  
def leadupdshow(request):
    leadid=request.POST.get('leadupdsearch')
    leads=crm3lead.objects.filter(leadid=leadid)
    return render(request,"leadupdshow.html",{'leads':leads})

def leadupdsearch(request):
    return render(request,'leadsearch.html')    

def leaddel(request):
    custid=request.POST.get('custdelsearch')
    customer=crm3cust.objects.filter(custid=custid)
    customer.delete()
    return render(request,"suc.html")

def leaddelsearch(request):
    return render(request,'custupdsearch.html')

def retsuc(request):
        return render(request,'suc.html')

def homepage(request):
        return render(request,'index.html')
