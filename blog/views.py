from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    return render(request, "list.html", {"posts": posts})


def post_detail(request, year, month, date, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=date,
    )

    return render(request, "detail.html", {"post": post})
