from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


state = 'ST'
news = 'NW'
POSITIONS = [(state, 'статья'), (news, 'новости')]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        author_rating = self.rating
        return author_rating


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    category = models.ManyToManyField(Category, through='PostCategory')
    choice = models.CharField(max_length=2, choices=POSITIONS)
    create_data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    head = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    slug = models.SlugField(max_length=128, unique=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    def like(self):
        add_like = self.rating
        return add_like + 1

    def dislike(self):
        add_dislike = self.dislike
        return add_dislike + 1

    def preview(self):
        return self.text(max_length=124) + '...'

    def __str__(self):
        return '{}'.format(self.head)

    class Meta:
        ordering = ['-create_data']


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    create_data = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        add_like = self.rating
        return add_like + 1

    def dislike(self):
        add_dislike = self.dislike
        return add_dislike + 1