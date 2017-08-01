from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RequestForm

from .models import Request

def index(request):
    test_list = Request.objects.order_by('Date')[:5]
    template = loader.get_template('purchase_requests/index.html')
    #output = ', '.join([q.part_number for q in test_list])
    context = {
        'test_list': test_list,
    }
    return HttpResponse(template.render(context, request))

def request_new(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.User = request.user
            post.Date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = RequestForm()
    return render(request, 'purchase_requests/post_edit.html', {'form': form}) 

