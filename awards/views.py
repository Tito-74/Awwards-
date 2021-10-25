from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import Review, Profile, Post
from django.contrib.auth.decorators import login_required
from awards.forms import PostForm, RatingsForm
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.urls import reverse



# Create your views here.

def awards(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'awards/awards.html', context)

def review(request, id):
    project = Post.objects.get(id=id)
    rate = Review.objects.filter(user=request.user, post=project).first()
    ratings = Review.objects.all()
    rating_status = None
    if rate is None:
        rating_status = False
    else:
        rating_status = True
    current_user = request.user
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['creativity']
            comment = form.cleaned_data['comment']
            review = Review()
            review.post = project
            review.user = current_user
            review.design = design
            review.usability = usability
            # review.creativity = creativity
            review.comment = comment
            review.average = (
            review.design + review.usability + review.creativity)/3
            review.save()
            return HttpResponseRedirect(reverse('review', args=(project.id,)))
    else:
        form = RatingsForm()
    params = {
        'project': project,
        'form': form,
        'rating_status': rating_status,
        'reviews': ratings,
        'ratings': rate
    }
    return render(request, 'awards/reviews.html', params)
    # return render(request, 'awards/reviews.html')

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

def search(request):
    return render(request, 'awards/search.html')

