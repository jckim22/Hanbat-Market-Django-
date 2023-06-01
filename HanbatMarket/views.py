from HanbatMarket.models import Board
from django.shortcuts import render,redirect
from .models import Board
from .forms import RegistForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count


def index(request):
    page = request.GET.get('page', '1')  # 페이지 파라미터 얻기, 없으면 1
    board_list = Board.objects.order_by('price')
    search = request.GET.get('search','')
    if search:
      board_list = board_list.filter(
      Q(title__icontains = search) | #제목
      Q(author__icontains = search) #글쓴이
    )
    # 페이징 처리
    paginator = Paginator(board_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)  # page에 해당하는 페이징 객체 생성

    context = {'board_list': page_obj,'search':search}   # 페이징 객체(page_obj) 전달
    return render(request, 'HanbatMarket/index.html', context)

def regist(request):
    if request.method == 'POST':
        form = RegistForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.seller = request.user  # 현재 로그인한 사용자를 writer로 고정시켜줘야함
            post.save()
            return redirect('hanbat_market:index')
    else:
        form = RegistForm()
    context = {'form': form,}
    return render(request, 'HanbatMarket/regist_form.html', context)


def detail(request, pk):
    board_list = get_object_or_404(Board, id=pk)
    context = {'board_list': board_list}
    return render(request, 'HanbatMarket/detail.html', context)

def edit(request, pk):
    post = get_object_or_404(Board, id=pk)
    if request.method == 'POST':
        form = RegistForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('hanbat_market:index')
    else:
        form = RegistForm(instance=post)
    context = {'form': form,}
    return render(request, 'HanbatMarket/edit_form.html', context)

def delete(request, pk):
    post = get_object_or_404(Board, id=pk)
    post.delete()
    return redirect('hanbat_market:index')