import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags
# Create your models here.

class Category(models.Model):
    '''
    这是文章的分类
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name

class Post(models.Model):
    #这是文章的标题
    title = models.CharField(max_length=70)
    #文章的正文，需要更大的存储，因此使用了TextField来存储

    images = models.ImageField(upload_to='static/blog/images/' ,blank = True)
    #这是文章的图片


    body = models.TextField()
    #这是文章的创建时间和修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    #作者
    auth = models.ForeignKey(User)


    def __str__(self):
        return  self.title
    #自定义了get_absolute_url函数
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time']
