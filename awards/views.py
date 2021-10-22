from django.shortcuts import render

# Create your views here.
def awards(request):
    return render(request, 'awards/award.html')

def review(request):
    return render(request, 'awards/review.html')

def addproject(request):
    return render(request, 'awards/add.html')

def search(request):
    return render(request, 'awards/search.html')

