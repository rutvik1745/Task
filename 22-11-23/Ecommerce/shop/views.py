from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact,Orders
from django.views import View
from math import ceil

# Create your views here.
class IndexView(View):
    def get(self,request):
        # products = Product.objects.all()
        # allProds=[[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
        # params={'allProds':allProds }
        allProds = []
        catprods = Product.objects.values('category','id')
        cats = {item['category']for item in catprods}
        print(cats)
        for cat in cats:
            prod = Product.objects.filter(category = cat)
            n = len(prod)
            nSlides = n//4 + ceil((n/4)-(n//4))
            allProds.append([prod,range(1,nSlides),
            nSlides])
        print(allProds)
        # params={'no_of_slides':nSlides,'range':range(1,   nSlides),
        #     'product':products}
        params = {"allProds":allProds}
        return render(request,'shop/index.html',params)

class ProductView(View):
    def get(self,request,myid):
        product = Product.objects.get(id=myid)
        print(product)
        return render(request,'shop/prodView.html',{'product':product})
    
def about(request):
    return render(request,'shop/about.html')

class ContactView(View):
    def get(self,request):
        return render(request,'shop/contact.html')
    def post(self,request):
        if request.method == "POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            desc = request.POST.get('desc', '')
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
            
        return render(request,'shop/contact.html')
def tracker(request):
     return render(request,'shop/tracker.html')


def search(request):
    return HttpResponse("We are at search")
class CheckoutView(View):
    def get(self, request):
        return render(request, 'shop/checkout.html')
    
    def post(self,request):
        if request.method == "POST":
            items_json = request.POST.get('itemsJson','')
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')
            phone = request.POST.get('phone', '')
            order = Orders(items_json= items_json ,name=name, email=email,address= address,city=city,state=state,zip_code=zip_code,phone=phone)
            order.save()
            thank = True
            id = order.order_id
            return render(request, 'shop/checkout.html',{'thank':thank, 'id':id})
        return render(request, 'shop/checkout.html')
