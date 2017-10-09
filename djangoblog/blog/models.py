from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='类别名')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类管理'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=100,verbose_name='标签名')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '标签管理'
        verbose_name_plural = verbose_name


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    modified_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')
    excerpt = models.CharField(max_length=200, null=True, blank=True,verbose_name='备注')
    tag = models.ManyToManyField(Tag, null=True, blank=True,verbose_name='标签')
    category = models.ForeignKey(Category, verbose_name='类别')
    author = models.ForeignKey(User, verbose_name='作者')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '博客管理'
        verbose_name_plural = verbose_name
        ordering=['-created_time']

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'pk': self.pk})


