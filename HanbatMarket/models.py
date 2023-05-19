from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=200, verbose_name='책 이름', help_text='* 책 제목은 정확하게 기입해주세요.')
    author = models.CharField(max_length=100, verbose_name='글쓴이')
    price = models.IntegerField(verbose_name='상품 가격')
    content = models.TextField(verbose_name='상품 설명')
    published_date = models.DateTimeField(auto_now=True, verbose_name='등록(수정)일')

    def __str__(self):
        return self.title