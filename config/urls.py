from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: redirect('hanbat_market:index')),
    path('hanket/', include('HanbatMarket.urls')),
    path('accounts/', include('allauth.urls')),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)