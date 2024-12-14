from django.shortcuts import render,HttpResponse
# from .models import Product, Cart
# from django.db.models import Q
from .models import Msg

# Create your views here.

def home(request):
    return HttpResponse("In home page")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contect page")

def product_details(request,pid):
    return render(request,'product_details.html',context)

def addtocart(request,pid):
    if request.user.is_authenticated:
        userid=request.user.id
        # print(userid)
        u=User.objects.get(id=userid)
        # print(pid)
        p=Product.objects.get(id=pid)
        # print(u,p)
        q1=Q(uid=u)
        q2=Q(pid=p)
        c=Cart.objects.filter(q1 & q2)
        print(c)
        n=len(c)
        context={}
        p=Product.objects.filter(id=pid)
        context['products']=p
        if n==1:
            context['errmsg']="Product Already Exsists in Cart!!!"
        else:
            c=Cart.objects.filter(uid=u,pid=p)
            c.save()
            context['success']="Product added Successfully"

        # c=Cart.objects.create(uid=userid,pid=pid)
        # c.save()
        # context{}
        # p=Product.objects.filter(id=pid)
        # context['products']=p
        
        return render(request,'product_details.html',context)
        #return HttpResponse("product added to the cart")
    else:
        return redirect('/login')

def viewcart(request):
    c=Cart.objects.filter(uid=request.user.id)
    print(c)
    s=0
    for x in c:
        s=s+x.pid.price
    np=len(c)
    context={}
    context['total']=s
    context['n']=np
    context['data']=c
    print(c[0])
    print(c[0].uid)
    print(c[0].uid.email)
    print(c[0].uid.is_superuser)
    print(c[0].pid)
    print(c[0].pid.price)
    print(c[0].pid.pdetails)
    #print(c[1])
    return render(request,'cart.html')

def remove(request,cid):

    c.delete()
    return redirect('/viewcart')

def updateqty(request,qv):
    if qv == '1':
        pass
    else:
        pass
    return redirect('/viewcart')

def placeorder(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    # print (c)
    oid=random