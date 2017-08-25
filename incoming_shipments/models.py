from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import TextInput 
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

class shipments(models.Model): #make a table with this info 
    ship_no = models.CharField(max_length=8, verbose_name="SHIP NO")
    supplier = models.CharField(max_length=30, verbose_name="Supplier")
    Port_ETA = models.CharField(max_length=8, verbose_name="Port ETA")
    Store_ETA = models.CharField(max_length=8, verbose_name="Into Store ETA")
    Comment = models.CharField(max_length=30, verbose_name="Comment")

