from django.shortcuts import render

# Create your views here.
def awards(request):
    return render(request, 'awards/awards.html')

def review(request):
    return render(request, 'awards/reviews.html')

def addproject(request):
    return render(request, 'awards/add.html')

def vote(request):
    return render(request, 'awards/vote.html')

def search(request):
    return render(request, 'awards/search.html')

