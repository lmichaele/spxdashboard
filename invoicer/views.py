from django.shortcuts import render
from django.http import HttpResponse

def invoicer(request):
    return render(request, "Documents.html")
