from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import Review, Profile, Post
from django.contrib.auth.decorators import login_required
from awards.forms import PostForm
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User



# Create your views here.

def awards(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'awards/awards.html', context)

def review(request):
    return render(request, 'awards/reviews.html')

@csrf_exempt
def addproject(request):
    

    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_project = form.save(commit=False)
            post_project.user = current_user
            post_project.save()
            return redirect('awards')
    else:
        form = PostForm()

    # print(form)
    return render(request, 'awards/add.html', {"form": form})


@login_required(login_url='/account/login')
def vote(request):
    return render(request, 'awards/vote.html')

def search(request):
    return render(request, 'awards/search.html')

