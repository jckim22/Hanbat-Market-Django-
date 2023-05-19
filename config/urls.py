from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: redirect('hanbat_market:index')),
    path('hanket/', include('HanbatMarket.urls')),
]