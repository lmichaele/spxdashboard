from django.http import Http404
from django.shortcuts import render

from .models import Request

def index(request):
    latest_request_list = Request.objects.order_by('-pub_date')[:5]
    context = {'latest_requests': latest_request_list}
    return render(request, 'purchase_requests/index.html', context)
