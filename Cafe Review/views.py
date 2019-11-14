from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Review
from .forms import ReviewForm

# Create your views here.

def index(request):
    return render(request, 'cafe/index.html')

#Pass Review model class to review template.
#Enables review.html to display all reviews.
def review(request):
    context = {'reviews': Review.objects}
    return render(request, 'cafe/review.html', context)

#Method to create a new review.
def leave_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return HttpResponseRedirect('/cafe/review/')
    else:
        form = ReviewForm()
    return render(request, 'cafe/leave_review.html', {'form': form})
