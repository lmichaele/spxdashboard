from django.conf import settings
from django.db import models
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
import logging

import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
import re, csv, os, shutil, xlsxwriter
from datetime import timedelta, datetime
import pandas as pd
import csv, codecs

from .models import Ennery_ConfirmPOLines
from .models import Sparex_Invoice

from .forms import Sparex_Invoicef
from .forms import Ennery_ConfirmPOLinesf

def invoicer(request):
    return render(request, "invoicer\Documents.html", {})


def xml_to_csv(request):

    data = {}

    try:
        xml_file = request.FILES["xml_file"]
        
        if not xml_file.name.endswith('XML'):
            messages.error(request,'File is not XML type')
            #return render(request, "invoicer\Documents.html", {})

        tree = ET.parse(xml_file)
        root = tree.getroot()

        for Line in root.findall('Line'):
            data_dict = {}
            data_dict['invoice'] = root[0][2].text
            data_dict['part'] = Line.find('PartNumberSupplied').text
            data_dict['qty'] = Line.find('QuantitySent').text
            data_dict['value'] = Line.find('UnitPrice').text
            data_dict['po'] = Line.find('CustomerOrderRef').text
            data_dict['eta'] = str((datetime.now() + timedelta(days=7)).strftime("%Y%m%d"))
            data_dict['tlv'] = (int(Line.find('QuantitySent').text)) * (float(Line.find('UnitPrice').text))

            form = Ennery_ConfirmPOLinesf(data_dict)
			

            try:
                if form.is_valid():
                    form.save()
                    
                else:
                    logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
                    #return render(request, "invoicer\Documents.html", {})

            except Exception as e:
                messages.error(request,'error2')
                logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
                return render(request, "invoicer\Documents.html", {})

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ConfirmPOLines.csv"'

        writer = csv.writer(response)

        invoice_lines = Ennery_ConfirmPOLines.objects.all().values_list('invoice','part','qty','value','po','eta','tlv')
        for line in invoice_lines:
            writer.writerow(line)
        Ennery_ConfirmPOLines.objects.all().delete()
        return response



    except Exception as e: #this is where browser is going after file upload... 
        messages.error(request,'error3')
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        
    return render(request, "invoicer\Documents.html", {})
    messages.error(request,'error4')
    #logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))

    return render(request, "invoicer\Documents.html", {})



def spx_invoice(request):

    data = {}

    if "GET" == request.method:
        return render(request, "invoicer\Documents.html", data)

    try:    
        sp_csv_file = request.FILES['sp_csv_file']
        #print(type(sp_csv_file))
        cnc = str(sp_csv_file)

        print(sp_csv_file.name)

        if not sp_csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV')
            return render(request, "invoicer\Documents.html", {})

        file_data = sp_csv_file.read().decode("utf-8")
        #print(type(file_data))
        #print(file_data)
     
        lines = file_data.split("\n")
        #print(type(lines))
        #print(lines)
            #loop over the lines and save them in db. If error , store as string and then display

        for line in lines:
            #print(type(line))                     
            fields = line.split(",")
            #print(fields[0])
            data_dict = {}
            
            if fields[0] == 'INH':
                example = 0

            elif fields[0] == 'IDH':
                
                invoice = fields[5]
                #data_dict["invoice"] = fields[5]


            elif fields[0] == 'IDD' and fields[1].isnumeric():
                #print("yes")
            
                data_dict["connection"] = cnc[0:9]
                data_dict["part"] = fields[1]
                data_dict["qty"] = fields[3]
                data_dict["value"] = round(float(fields[6]) / float(fields[3]),2)
                data_dict["po"] = fields[7]
                data_dict["eta"] = str((datetime.now() + timedelta(days=7)).strftime("%Y%m%d"))
                data_dict["invoice"] = invoice

            
                #data_dict["invoice"] = fields[6]

            #else: 
                #print(fields[0])
                #logging.getLogger("error_logger").error("Unable to upload file.")
                #return render(request, "invoicer\Documents.html", {})
            
            #data_dict["tlv"] = fields[2]
            
            #return render(request, "invoicer\Documents.html", {'form':form})
        
            try:
                #print(data_dict)
                form1 = Sparex_Invoicef(data_dict)
                if form1.is_valid():
                    form1.save()

                else:
                    messages.error(request,'Form is invalid')
                        
            except Exception as e:
                messages.error(request,'error2')
                logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
                return render(request, "invoicer\Documents.html", {})

            

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ConfirmPOLines.csv"'

        writer = csv.writer(response)

        invoice_lines = Sparex_Invoice.objects.all().values_list('connection','part','qty','value','po','eta','invoice')
        
        for line in invoice_lines:
            writer.writerow(line)
        Sparex_Invoice.objects.all().delete()
        return response



    except Exception as e: #this is where browser is going after file upload... 
        messages.error(request,'error3')
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        
    return render(request, "invoicer\Documents.html", {})
    messages.error(request,'error4')
    #logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))

    #Ennery_ConfirmPOLines.objects.all().delete()
    #return render(request, "invoicer\Documents.html", {})