from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from users.models import Comment


class PostListView(ListView):
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(is_active=True)


def single_post(request, post_id):
    post = Post.objects.filter(id=post_id)[0]
    comments = Comment.objects.filter(post=post)
    if request.POST:
        comment = Comment.objects.create(user=request.user, post=post, comment=request.POST.get('comment'))

    return render(request, 'posts/single_post.html', locals())
