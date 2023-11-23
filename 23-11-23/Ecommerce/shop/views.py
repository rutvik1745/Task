from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact,Orders,OderUpdate
from django.views import View
import json
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

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

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
        thank = False
        if request.method == "POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            desc = request.POST.get('desc', '')
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            thank = True
        return render(request,'shop/contact.html',{'thank':thank})
    

class TrackerView(View):
    def get(self, request):
        return render(request,'shop/tracker.html')
     
    def post(self,request):
        if request.method=="POST":
            orderId = request.POST.get('orderId', '')
            email = request.POST.get('email', '')
            try:
                order = Orders.objects.filter(order_id=orderId, email=email)
                if len(order)>0:
                    update = OderUpdate.objects.filter(order_id=orderId)
                    updates = []
                    for item in update:
                        updates.append({'text': item.update_desc, 'time': item.timestamp})
                        response = json.dumps([updates, order[0].items_json], default=str)
                    return HttpResponse(response)
                else:
                    return HttpResponse('{"status":"noitem"}')
            except Exception as e:
                return HttpResponse('{"status":"error"}')

        return render(request, 'shop/tracker.html')






class CheckoutView(View):
    def get(self, request):
        return render(request, 'shop/checkout.html')
    
    def post(self,request):
        if request.method == "POST":
            items_json = request.POST.get('itemsJson','')
            name = request.POST.get('name', '')
            amount = request.POST.get('amount', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')
            phone = request.POST.get('phone', '')
            order = Orders(items_json= items_json ,name=name, email=email,address= address,city=city,state=state,zip_code=zip_code,phone=phone, amount=amount)
            order.save()
            update = OderUpdate(order_id = order.order_id,update_desc="The order has been placed")
            update.save()
            thank = True
            id = order.order_id
            return render(request, 'shop/checkout.html',{'thank':thank, 'id':id})
        return render(request, 'shop/checkout.html')

