from django.db import models
from django.contrib.auth.models import User
from posts.models import *


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, default=None, verbose_name='Пост')
    comment = models.CharField(max_length=128, blank=True, null=False, default=None, verbose_name='Комметарий')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return "%s : %s" % (self.user.username, self.post.name)



