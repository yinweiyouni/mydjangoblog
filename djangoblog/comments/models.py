from django.db import models

# Create your models here.


class Comments(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    email = models.EmailField(max_length=255, verbose_name='邮箱')
    url = models.CharField(max_length=100, null=True, blank=True, verbose_name='网址')
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论日期')
    post = models.ForeignKey('blog.Blog')

    def __unicode__(self):
        return self.text[:20]

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
