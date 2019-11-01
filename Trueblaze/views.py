from .forms import CommentForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from.models import Comment


def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments': comments}
    return render(request, 'Trueblaze/index.html', context)


def sign(request):
    if request.method != 'POST':
        # no data submitted, create a blank form
        form = CommentForm
    else:
        # post data submitted; process data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return HttpResponseRedirect(reverse('Trueblaze:index'))
    context = {'form': form}
    return render(request, 'Trueblaze/sign.html', context)


def about(request):
    context = {'request': request}
    return render(request, 'Trueblaze/about.html', context)


def portfolio(request):
    context = {'request': request}
    return render(request, 'Trueblaze/portfolio.html', context)
