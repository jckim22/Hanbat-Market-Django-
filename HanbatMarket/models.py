from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from HanbatMarket.models import User

class Board(models.Model): #Book Table
    title = models.CharField(max_length=200, verbose_name='상품명', help_text='* 책 제목은 정확하게 기입해주세요.')
    author = models.CharField(max_length=100, verbose_name='저자')
    seller = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete : User가 delete 될 때 게시글을 어떻게 설정한 것인지에 대해 설정 1. 게시글 같이 지우기(CASCADE) 2. 없는 값으로 해서 게시글은 남겨두기
    publisher = models.CharField(max_length=100, verbose_name='출판사')
    minPrice = models.IntegerField(verbose_name='최소구매가')
    maxPrice = models.IntegerField(verbose_name='최대구매가')
    kakaoId = models.CharField(max_length=100, verbose_name='판매자의 kakaoId 또는 전화번호', help_text='* 구매자와의 연락을 위한 정보를 기입해주세요.')
    imgfile = models.ImageField(null=True, upload_to="", blank=True,verbose_name='상품 사진') # 이미지 컬럼 추가
    content = models.TextField(verbose_name='상품 설명')
    published_date = models.DateTimeField(auto_now=True, verbose_name='등록(수정)일')
    under_line = models.BooleanField(verbose_name='밑줄 유무')
    written = models.BooleanField(verbose_name='필기 유무')
    page_named = models.BooleanField(verbose_name='이름 기입')
    page_age = models.BooleanField(verbose_name='페이지 변색')
    ripped = models.BooleanField(verbose_name='페이지 훼손')
    

    def __str__(self):
        return self.title
    
    
