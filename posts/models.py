from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=64, blank=True, null=False, default=None, verbose_name='Имя')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
    name = models.CharField(max_length=128, blank=True, null=False, default=None, verbose_name='Заголовок')
    is_active = models.BooleanField(default=True)
    content = models.CharField(max_length=512, blank=True, null=False, default=None, verbose_name='Текст')
    image = models.ImageField(upload_to='posts/img/', blank=True, null=True, default=None, verbose_name='Картинка')
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, null=True, default=None, verbose_name='Теги')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

