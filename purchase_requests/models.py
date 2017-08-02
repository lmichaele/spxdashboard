from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import TextInput 
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible

class Request(models.Model): #part, qty, WH, User, Date
    part_number = models.CharField(max_length=30, verbose_name="Part Number")
    qty = models.IntegerField(default=0)
    WH = models.CharField(max_length=3) #change to checkboxes/radiobuttons to save multiple lines w same part for different warehosues
    User = models.ForeignKey('auth.User')
    Date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.part_number
        


class UUTForm(ModelForm):
    class Meta:
        model = Request
        widgets = {
            'comments': TextInput(attrs={'size': 10}),
        }
        fields = ['part_number', 'qty', 'WH', 'User', 'Date']

