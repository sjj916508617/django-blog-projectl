from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Comment
from .forms import CommentForm



def get_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            comment.save()
        else:
            pass

    post_get = Comment.objects.all()
    paginator = Paginator(post_get,6)
    try:
        page =int(request.GET.get('page',1))
        post_get = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        post_get = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        post_get = paginator.page(paginator.num_pages)

    return render(request, 'blog/guestbook.html',context={'post_get':post_get})
