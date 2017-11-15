from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from .models import Post
import markdown

#首页视图
def index(request):
    post_list = Post.objects.all()[1:5]
    return render(request,'blog/index.html',context={'post_list':post_list})
#文章详情页
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,extensions=['markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc'
                                                        ])
    return render(request,'blog/detail.html',context={'post':post})

#关于我页面
def post_simple(request):
    return render(request, 'blog/aboutme.html')

#相册的页面
def post_xc(request):
    return render(request, 'blog/xc.html')

#分页内容
def index_all(request):
    post_list2 = Post.objects.all()
    paginator = Paginator(post_list2, 4)  # 每页显示 25 个联系人

    try:
        page =int(request.GET.get('page',1))
        post_list2 = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        post_list2 = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        post_list2 = paginator.page(paginator.num_pages)

    return render(request,'blog/shuo.html',context={'post_list2':post_list2})
