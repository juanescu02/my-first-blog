from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.form import UserCreationForm
from django.views.generic import Created View
from .models import Post
from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
