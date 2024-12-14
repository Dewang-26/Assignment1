"""
URL configuration for envt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
# from . import views
# from messages import settings
# from django.conf.urls.static if

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('delete/<rid>',views.delete),
#     path('',views.home),
#     path('pdetails',views.product_details)
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(message_app.urls))
    # path('about',views.about),
    # path('contact',views.contact),
    # path('home',views.home)
    # path('create',views.create)
    # path('admin/', admin.site.urls),
    # path('delete/<rid>',views.delete),
    # #path('',views.home),
    # #path('pdetails',views.product_detailss),
    # path('delete/<rid>',views.delete),
    # path('addition/<x>/<y>',views.addition),
    # path('myview',views.SimpleView.as_view()),
    # path('hello',views.hello),
    # path('register',views.register),
    # path('login',views.user_login)
    # path('logout',views.user_logout),
    # path('catfilter/<cv>',views.catfilter),
    # path('sort/<sv>',views.sort)
    # path('range',views.range)
    #path('pdetails/','')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
                

def product_details(request,pid):
    p=Product.object.filter(id=pid)     #id=4=> [<object 4>]
    context={}
    context['products']=p
    return render(request,'product_details.html',context)

