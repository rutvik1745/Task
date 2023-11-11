from django.shortcuts import render,redirect
from .models import punch1
from datetime import datetime
from datetime import datetime
from django.views import View
from datetime import date




def index(request): 
    return render(request,"index.html") 
def star(request): 
        # print("jadfu")
        d = date.today()
        # print(d,"This is a date")
        s = datetime.now()
        # print(s, "This is cthe courretnt time")
        t = punch1(startWork = s, endWork=s)
        productList = punch1.objects.filter().values()
        print(productList)
        da=[]
        for w in productList:
            # print(w)
            # print(w['startWork'])
            # print(w['startWork'].date())
            da.append(w['startWork'].date())

        # print(da,"this is a date list")
        if len(da) == 0:
             t.save()
        else:
            for i in da: 
                if i != d:
                      t.save()  
        return redirect("about") 

    #     return render(request, "index.html") 
def about(request): 
    return render(request,"about.html") 


def end(request): 
        print("jadfu")
        d = date.today()
        s = datetime.now()
        productList = punch1.objects.filter().values()
        print(productList)
        for i in productList:
             x =i['startWork']
    
        print(s, "This is cthe courretnt time")
        e = punch1(startWork=x,endWork = s)
        e.save()
        productList = punch1.objects.filter().values()
        for i in productList:
             k =i['startWork']
             y = i['endWork']
            #  z= k-y
        k=k.time()
        y=y.time()
        k = str(k)
        y = str(y)
        k = datetime.strptime(k,"%H:%M:%S.%f")
        y = datetime.strptime(y,"%H:%M:%S.%f")
        z= y-k
        print(z)


        print(z,'this is a total')
        
        return render(request,"end.html") 
