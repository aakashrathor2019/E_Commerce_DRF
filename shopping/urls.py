from django.contrib import admin
from django.urls import path 
from  . views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required




urlpatterns=[
    path("admin/",admin.site.urls),
    path('add_product/',AddProduct.as_view(),name='add_product'),
    
]

