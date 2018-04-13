from django import forms

from .models import Ennery_ConfirmPOLines
from .models import Sparex_Invoice

class Ennery_ConfirmPOLinesf(forms.ModelForm):

    class Meta:
        model = Ennery_ConfirmPOLines
        fields = ('invoice', 'part', 'qty', 'value', 'po', 'eta', 'tlv')


class Sparex_Invoicef(forms.ModelForm):

    class Meta:
        model = Sparex_Invoice
        fields = ('connection', 'part', 'qty', 'value', 'po', 'eta', 'invoice')