from ..models import Blog, Category, Tag
from django import template

register = template.Library()


@register.simple_tag
def get_recent_post(num=5):
    return Blog.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Blog.objects.dates('created_time', 'month', 'DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()





