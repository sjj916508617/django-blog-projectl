#! /usr/bin/env python
#coding = utf-8
'''
自定义模板标签
'''

from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    #获取最新的五篇文章
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_random_posts(num=5):
    #随机获取文章
    return Post.objects.all().order_by('?')[:5]


@register.simple_tag
def get_recommend_posts(num=5):
    #获取推荐五篇文章
    return Post.objects.all().order_by('created_time')[1:6]
