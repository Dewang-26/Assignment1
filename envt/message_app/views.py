from django.shortcuts import render,HttpResponse,redirect
# from django.views import view
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login, logout
# from message_app.models import Msg
from . models import Msg

# Create your views here.
#from django.shortcuts import render, HttpResponse
#from django.http import HttpResponse
# from .models import Msg


def home(request):
    return HttpResponse("In home page")

# def about(request):
# 	return HttpResponse("This is about page")

# def contact(request):
#     return HttpResponse("This is contacts page")

# def create(request):
#     #print ("Request is:",request.method)
#     if request.method=='POST':     #imp
#         n=request.POST['uname']
#         mail=request.POST['uemail']
#         mob=request.POST['mobile']
#         msg=request.POST['msg']
#         #print("Name:",n)
#         #print("Message:",msg)
#         m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
#         #m.save()
#         return HttpResponse("Data fetched Inserted successfully")
#         #fetch data from form
#         #pass
#         #return redirect('/')
#     else:
#         return render(request,'create.html')

# def dashboard(request):
#     m=Msg.objects.all()     #2 objects
#     #print(m)               #list format
#     context={}
#     context['data']=m
#     return render(request,'dashboard.html',context)
#     #return HttpResponse("Data fetched from Databases")

# def delete(request,rid):
#     m=Msg.objects.filter(id=rid)
#     #print(m)
#     m.delete()
#     return redirect('/')
#     #return HttpResponse("Id to be deleted"+ rid)

# def edit(request,rid):
#     if request.method=='POST':
#         n=request.POST['uemail']
#         mail=request.POST['uemail']
#         mob=request.POST['mobile']
#         msg=request.POST['msg']
#         print(n,'-',mail,'-',mob,'-',msg)
#         return HttpResponse("Data updated")
#     else:
#         #display from with previous values
#         # m=Msg.objects.filter(id=rid) #<Querset  [<Msg: Msg object  (4)>]
#         m=Msg.objects.get(id=rid)    #Msg: Msg object (4)>
#         print(m)
#         context={}
#         context['data']=m
#         return render(request,'edit.html',context)
#     # return HttpResponse("Id to be edited"+rid)

# def product_details(request):
#     return render(request,'product_detailss.html')

# def register(request):
#     if request.method=='POST':
#         uname=request.POST['uname']
#         upass=request.POST['upass']
#         ucpass=request.POST['ucpass']
#         context={}
#         if uname=="" or upass=="" or ucpass="":
#             context['errmsg']="Fields cannot be empty"
#         elif upass != ucpass:
#             context['errmsg']="password and confirm password didnt matched!!"
#         else:
#             u=User.objects.create(password=upass,username)
#             u.set_pasword(upass)
#             u.save()
#             context['success']="User Created successfully"
#         except Exception:
#             context['errmsg']="Fields cannot be empty"
#             elif upass != ucpass:
#                 context['errmsg']="password and confirm password didnt matched!!"
#             else:
#                 try:
#                     u=User.objects.create(password=upass,username=uname,email=uname)
#                     u.set_password(upass)
#                     u.save()
#                     context['success']="User Created successfully"
#                 except Exception:
#                     context['errmsg']="User with same Username already  exists!!"

#         return render(request,'register.html',context)
#         #     u=User.objects.create(password=upass,username=uname,email=uname)
#         #     u.save()
#         # return HttpResponse("Data is fetched"+ uname)
#     else:
#         return render(request,'register.html')

# def user_login(request):
#     if request.method=='POST':
#         uname=request.POST['uname'] #""
#         upass=request.POST['upass']
#         context={}
#         if uname=="" or upass=="":
#             context['errmsg']="Fields cannot be empty"
#             return render(request,'login.html',context)
#         else:
#             u=authenticate(userrname=uname,password=upass)
#             print(u)
#             return HttpResponse("Data fetched")
#             return HttpResponse(uname)
#     else:
#         return render(request,'login.html')
        
# def user_login(request):
#     if request.method=='POST':
#         uname=request.POST['uname'] #""
#         upass=request.POST['upass']
#         context={}
#         if uname=="" or upass=="":
#             context['errmsg']="Fields cannot be empty"
#             return render(request,'login.html',context)
#         else:
#             u=authenticate(userrname=uname,password=upass)
#             if u is not None:
#                 login(request,u)    #session start
#                 return redirect('/')    #home page
#             else:
#                 context['errmsg']="Invalid Username & Password"
#                 return renderr(request,'login.html',context)
#         else:
#             return render(request,'login.html')

# #estore project--------
# def home(request):
#     #userid=request.user.id  #3
#     #print("logged in userid:",userid)
#     print(request.use.is_authenticated)
#     context={}
#     p=Product.objects.filter(is_active=True)    #6objects
#     print(p)
#     context['products']=p
#     return render(request,'index.html',context)

# def product_details(request):
#     return render(request,'product_details.html')

# def register(request):
#     else:
#         return render(request,'')

# def user_logout(request):
#     logout(request)
#     return redirect('/')

# def catfilter(request,cv):
#     q1=Q(is_active=True)
#     q2=Q(cat=cv)
#     p=Product.objects.filter(q1 & q2)
#     print(p)        #2 objects
#     context={}
#     context['products']=page
#     return render(request,'index.html',context)

# def sort(request,sv):
#     if sv =='0':
#         col='price'
#         pass
#     else:
#         col='-price'
#     p=Product.objects.filter(is_active=True).order_by(col)
#     context={}
#     context['products']=p
#     return render(request,'index.html',context)

# # 6-12-2024
# def range(request):
#     min=request.GET['min']
#     max=request.GET['max']
#     q1=Q(price__gte=min)
#     q2=Q(price__lte=max)
#     q3=Q(is_active=True)
#     p=Product.objects.filter(q1 & q2 & q3)
#     context={}
#     context['products']=p
#     return render(request,'index.html',context)
def viewcart(request):
    c=Cart.objects.filter(uid=request.user.id)
    #print(c)
    s=0
    for x in c:
        # print(x.pid.price)
        s=s+x.pid.price*x.qty
    np=len(c)
    context(c)
    context['total']=same
    context['n']=np
    context['data']=c
    return render(request,'cart.html',context)

def remove(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/viewcart')

def updateqty(request,qv,cid):
    c=Cart.objects.filter(id=cid)   #5 object
    print(c[0])
    print(c[0].qty)
    if qv == '1':
        t=c[0].qty+1
        c.update(qty=t)
        # pass
    else:
        if c[0].qty>1:
            t=c[0].qty-1
        c.update(qty=t)
        # pass
    return redirect('/viewcart')

def placeorder(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    # print(c)
    oid=random.randrange(1000,9999)
    print(oid)
    for x in c:
        o=Order.objects.create(order_id=oid,pid=x.pid,uid=x.uid,qty=x.qty)
        o.save()
        x.delete()
    orders=Order.objects.filter(uid=request.user.id)
    context={}
    context['data']=orders
    np=len(orders)
    s=0
    for x in orders:
        s=s+x.pid.price * x.qty
    context['total']=s
    context['n']=np
    return render(request,'placeorder.html',context)

        # print(x)
        # print(x.uid)
        # print(x.pid)
        # print(x.qty)
    # return HttpResponse("placeorder")

def makepayement(request):
    pass
