from django.shortcuts import render, get_object_or_404, redirect
from .models import Diary
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def get_diary(request):
    post_list_diary = Diary.objects.all()
    paginator = Paginator(post_list_diary, 6)
    try:
        page = int(request.GET.get('page', 1))
        post_list_diary = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        post_list_diary = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        post_list_diary = paginator.page(paginator.num_pages)

    return render(request, 'blog/diary.html',context={'post_list_diary':post_list_diary})
