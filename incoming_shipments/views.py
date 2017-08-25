from django.conf import settings
from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import shipments


def incoming_shipments(request):
    queryset = shipments.objects.all().order_by('ship_no')
    context = {
        "queryset": queryset,
    }
    return render(request, "incoming_shipments/incoming_shipments.html", context)
