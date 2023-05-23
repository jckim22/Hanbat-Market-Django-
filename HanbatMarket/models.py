from django.db import models

class Board(models.Model): #Book Table
    title = models.CharField(max_length=200, verbose_name='책 이름', help_text='* 책 제목은 정확하게 기입해주세요.')
    author = models.CharField(max_length=100, verbose_name='저자')
    seller = models.CharField(max_length=100, verbose_name="판매자")
    publisher = models.CharField(max_length=100, verbose_name='출판사')
    price = models.IntegerField(verbose_name='정가')
    content = models.TextField(verbose_name='상품 설명')
    published_date = models.DateTimeField(auto_now=True, verbose_name='등록(수정)일')
    under_line = models.BooleanField(verbose_name='밑줄 유무')
    written = models.BooleanField(verbose_name='필기 유무')
    page_named = models.BooleanField(verbose_name='이름 기입')
    page_age = models.BooleanField(verbose_name='페이지 변색')
    ripped = models.BooleanField(verbose_name='페이지 훼손')
    

    def __str__(self):
        return self.title