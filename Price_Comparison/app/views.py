from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.db.models import Max,Min,Count,Avg


def home(request):
    Model=Product.objects.all().order_by('-id')
    brand=Brand.objects.all().order_by('-id')
    return render(request, 'main/index.html',{'Model':Model,'brand':brand})

def product_detail(request):
 return render(request, 'main/index.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
    # brand = Brand.objects.all()
    Models=Product.objects.all().order_by('-id')
    brand = Product.objects.distinct().values('brand__title','brand__id')
    RAM = Product.objects.distinct().values('RAM__title','RAM__id')
    InternalStorage = Product.objects.distinct().values('InternalStorage__title','InternalStorage__id')
    BatteryCapacity = Product.objects.distinct().values('BatteryCapacity__title','BatteryCapacity__id')
    ScreenSize = Product.objects.distinct().values('ScreenSize__title','ScreenSize__id')
    PrimaryRearCamera = Product.objects.distinct().values('PrimaryRearCamera__title','PrimaryRearCamera__id')
    FrontCamera = Product.objects.distinct().values('FrontCamera__title','FrontCamera__id')
    OperatingSystem = Product.objects.distinct().values('OperatingSystem__title','OperatingSystem__id')
    NetworkConnectivity = Product.objects.distinct().values('NetworkConnectivity__title','NetworkConnectivity__id')
    ProcessorSpeed = Product.objects.distinct().values('ProcessorSpeed__title','ProcessorSpeed__id')
    NumberOfCores = Product.objects.distinct().values('NumberOfCores__title','NumberOfCores__id')
    Availability = Product.objects.distinct().values('Availability__title','Availability__id')
    minMaxPrice = Specifications.objects.aggregate(Min('Price_in_india'),Max('Price_in_india'))
    p = Paginator(Product.objects.all().order_by('-id'),8)
    page = request.GET.get('page')
    Model = p.get_page(page)
    return render(request, 'main/mobile.html',{'Model':Model,
    'Brand':brand,'RAM':RAM,'InternalStorage':InternalStorage,'BatteryCapacity':BatteryCapacity,
    'ScreenSize':ScreenSize,'PrimaryRearCamera':PrimaryRearCamera,'FrontCamera':FrontCamera,'OperatingSystem':OperatingSystem,
    'NetworkConnectivity':NetworkConnectivity,'ProcessorSpeed':ProcessorSpeed,'NumberOfCores':NumberOfCores,'Availability':Availability,'minMaxPrice':minMaxPrice})

def filter_data(request):
    brand =request.GET.getlist('brand[]')
    RAM =request.GET.getlist('RAM[]')
    InternalStorage =request.GET.getlist('InternalStorage[]')
    BatteryCapacity =request.GET.getlist('BatteryCapacity[]')
    ScreenSize =request.GET.getlist('ScreenSize[]')
    PrimaryRearCamera =request.GET.getlist('PrimaryRearCamera[]')
    FrontCamera =request.GET.getlist('FrontCamera[]')
    OperatingSystem =request.GET.getlist('OperatingSystem[]')
    NetworkConnectivity =request.GET.getlist('NetworkConnectivity[]')
    ProcessorSpeed =request.GET.getlist('ProcessorSpeed[]')
    NumberOfCores =request.GET.getlist('NumberOfCores[]')
    Availability =request.GET.getlist('Availability[]')
    minPrice=request.GET['minPrice']
    maxPrice=request.GET['maxPrice']
    allProduct=Product.objects.all().order_by('-id').distinct()
    allProduct=allProduct.filter(specifications__Price_in_india__gte=minPrice)
    allProduct=allProduct.filter(specifications__Price_in_india__lte=maxPrice)
    if len(brand)>0:
        allProduct=allProduct.filter(brand__id__in=brand).distinct()
    if len(RAM)>0:
        allProduct=allProduct.filter(RAM__id__in=RAM).distinct()
    if len(InternalStorage)>0:
        allProduct=allProduct.filter(InternalStorage__id__in=InternalStorage).distinct()
    if len(BatteryCapacity)>0:
        allProduct=allProduct.filter(BatteryCapacity__id__in=BatteryCapacity).distinct()
    if len(ScreenSize)>0:
        allProduct=allProduct.filter(ScreenSize__id__in=ScreenSize).distinct()
    if len(PrimaryRearCamera)>0:
        allProduct=allProduct.filter(PrimaryRearCamera__id__in=PrimaryRearCamera).distinct()
    if len(FrontCamera)>0:
        allProduct=allProduct.filter(FrontCamera__id__in=FrontCamera).distinct()
    if len(OperatingSystem)>0:
        allProduct=allProduct.filter(OperatingSystem__id__in=OperatingSystem).distinct()
    if len(NetworkConnectivity)>0:
        allProduct=allProduct.filter(NetworkConnectivity__id__in=NetworkConnectivity).distinct()
    if len(ProcessorSpeed)>0:
        allProduct=allProduct.filter(ProcessorSpeed__id__in=ProcessorSpeed).distinct()
    if len(NumberOfCores)>0:
        allProduct=allProduct.filter(NumberOfCores__id__in=NumberOfCores).distinct()
    if len(Availability)>0:
        allProduct=allProduct.filter(Availability__id__in=Availability).distinct()
    t=render_to_string('main/ajax/mobile.html',{'data':allProduct})
    return JsonResponse({'data':t})
def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def category_list(request,title =None):
    if(title == None):
        brands=Brand.objects.all().order_by('-id')
        p = Paginator(Brand.objects.all(),8)
        page = request.GET.get('page')
        brand = p.get_page(page)
        return render(request, 'main/Brands.html',{'brand':brand})
    else:
        brands=Brand.objects.filter(title=title)
        product=Product.objects.filter(brand__in=brands).order_by('-id')
        return render(request, 'main/Categoryfilter.html',{'Product':product,'brand':brands})

def specification(request,Model,id):
    specification = Specifications.objects.get(Model=id)
    product_img = Product_img.objects.filter(Model=id)
    return render(request,'main/Specifications.html',{'detail':specification ,'Product_img':product_img})

def search(request):
	q=request.GET['q']
	data=Product.objects.filter(Model__icontains=q).order_by('-id')
	return render(request,'main/search.html',{'data':data})
# def category_list(request,title):
    
