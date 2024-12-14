from django.urls import path
from . import views

#from myapp import views
# from ecomm import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('home',views.home)
#     path('create',views.create)
#     path('',views.dashboard)
#     path('delete/<rid>',views.delete)
#     path('edit/<rid>',views.edit)
#     path()
#     path('logout',views.user_logout)
#     path()
# ]

# if settings.DEBUG:

urlpatterns = [
    path('sort/<sv>',views.sort),
    path('range',views.range),
    path('pdetails/<pid>',views.product_details),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',view.viewcart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path()
    path('',views.makepayement)

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


