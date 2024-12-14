from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from myapp.models import Msg #app name should be given


# Create your views here.

def about(request):
	return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contacts page")

def home(request):
    return HttpResponse("In home page")

def create(request):
    #print ("Request is:",request.method)
    if request.method=='POST':
        # fetch data from form
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        print("Name:",n)
        print("Message:",msg)
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return HttpResponse("Data fetched successfully"+n)
    #     #fetch data from form
        # pass
    #     #return reddirect('/')
    else:
        return render(request,'create.html')

def footer(request):
    return render(request,'footer.html')

