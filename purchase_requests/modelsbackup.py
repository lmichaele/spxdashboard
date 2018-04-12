from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import TextInput 
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.conf import settings


class Request(models.Model): #part, qty, WH, OTP, User, Date
    part_number = models.CharField(max_length=30, verbose_name="Part Number")
    qty = models.IntegerField(default=0)
    SVI = 'SVI'
    SQL = 'SQL'
    SNW = 'SNW'
    SWA = 'SWA'
    WH_CHOICES = (
        (SVI, 'SVI'),
        (SQL, 'SQL'),
        (SNW, 'SNW'),
        (SWA, 'SWA'),
        )
    WH = models.CharField(max_length=3, choices=WH_CHOICES,
                          default=SVI)
    AIR = 'AIR'
    SEA = 'SEA'
    LOC = 'LOC' 
    OTP_CHOICES = (
        (AIR, 'AIR'),
        (SEA, 'SEA'),
        (LOC, 'LOC'),
        )
    OTP = models.CharField(max_length=3,
                           choices=OTP_CHOICES,
                           default=AIR, verbose_name="Order Type")
    User = models.ForeignKey(settings.AUTH_USER_MODEL)
    Date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.part_number
        

class UUTForm(ModelForm):
    class Meta:
        model = Request
        widgets = {
            'comments': TextInput(attrs={'size': 10}),
        }
        fields = ['part_number', 'qty', 'WH', 'OTP']


