from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','kakaoId', 'minPrice','maxPrice', 'author', 'published_date']
    list_display_links = ['id', 'title','kakaoId']
    list_per_page = 10