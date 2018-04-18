from django.conf import settings
from django.db import models
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from .forms import RequestForm
import logging
from django.contrib import messages
import csv, codecs
import io
from io import StringIO
from collections import defaultdict
import logging

from .models import Request, UUTForm


def index(request):
    return render(request, "purchase_requests/index.html")

def upload(request):
    return render(request, "purchase_requests/upload.html")


def request_new(request):
    #title = 'Add Purchase Request'
    form = RequestForm(request.POST)
    queryset = Request.objects.all().order_by('Date')
    context = {
    #"title": title,
    "form": form,
    "queryset": queryset,
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance_id = instance.id
        instance.User = request.user
        instance.save()

        
        context = {
            "queryset": queryset,
            "form" : form # pass the form in the context
        }

    return render(request, "purchase_requests/forms.html", context)


def upload_csv(request):
    
    data = {}

    try:    
        csv_file = request.FILES['csv_file']
        print(type(csv_file))
        print(csv_file)

        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            #return HttpResponseRedirect(reverse('/'))    

        file_data = csv_file.read().decode("utf-8")
        print(type(file_data))
        print(file_data)  
     
        lines = file_data.split("\n")
        print(lines)
        print(type(lines))
            #loop over the lines and save them in db. If error , store as string and then display

        for line in lines:
            print(line)                        
            print(type(line))
            fields = line.split(",")
            data_dict = {}
            data_dict["part_number"] = fields[0]
            data_dict["qty"] = fields[1]
            data_dict["WH"] = fields[2]
            data_dict["OTP"] = fields[3]
            
            form = RequestForm(data_dict)
            queryset = Request.objects.all().order_by('Date')
            context = {
            #"title": title,
            "form": form,
            "queryset": queryset,
            }
            
            try:
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.User = request.user
                    instance_id = instance.id
                    instance.save()

                    context = {
                        "queryset": queryset,
                        "form" : form # pass the form in the context
                    }
                else:
                    messages.error(request,'Please check CSV is correct format')

            except Exception as e:
                logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
                messages.error(request,'Beware the Double Dog')                   
                pass                            
    

    except Exception as e:
        pass
        #logging.getLogger("error_logger").error("Unable to upload file. Please check.")
        #messages.error(request,"Unable to upload file. "+repr(e))
    #return render(request, "purchase_requests/forms.html", context)
    next = request.POST.get('next', '/purchase_requests')

    return HttpResponseRedirect(next)

def function(request, part_id =None):
    object = Request.objects.get(id=part_id)
    object.delete()
    form = RequestForm(request.POST)
    queryset = Request.objects.all().order_by('Date')
    context = {
    #"title": title,
    "form": form,
    "queryset": queryset,
    }
    return render(request, "purchase_requests/forms.html", context)
