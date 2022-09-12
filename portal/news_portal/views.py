from django.shortcuts import render
from .models import Post


# Create your views here.
def default(request):
    news = Post.objects.all()
    return render(request, 'default.html', context={'news': news})


def detail(request, slug):
    new = Post.objects.get(slug__iexact=slug)
    return render(request, 'detail.html', context={'new': new})