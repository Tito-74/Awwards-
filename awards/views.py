from django.shortcuts import render
from .models import Review, Profile, Post

# Create your views here.
def awards(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'awards/awards.html', context)

def review(request):
    return render(request, 'awards/reviews.html')

def addproject(request):
    return render(request, 'awards/add.html')

def vote(request):
    return render(request, 'awards/vote.html')

def search(request):
    return render(request, 'awards/search.html')

