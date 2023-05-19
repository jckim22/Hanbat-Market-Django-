from django.urls import path
from . import views

app_name = 'hanbat_market'

urlpatterns = [
    path('', views.index, name='index'),
    path('regist/', views.regist, name='regist'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]