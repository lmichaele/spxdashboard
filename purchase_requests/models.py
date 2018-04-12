from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import TextInput 
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.conf import settings

class Request(models.Model): #part, qty, WH, User, Date
    part_number = models.CharField(max_length=30, verbose_name="Part Number")
    qty = models.IntegerField(default=0)
    WH = models.CharField(max_length=3) #change to checkboxes/radiobuttons to save multiple lines w same part for different warehosues
    OTP = models.CharField(max_length=3) 
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    Date = models.DateField(default=timezone.now) #add order type & comments
    def __str__(self):
        return self.part_number
        


class UUTForm(ModelForm):
    class Meta:
        model = Request
        widgets = {
            'comments': TextInput(attrs={'size': 10}),
        }
        fields = ['part_number', 'qty', 'WH', 'OTP']
