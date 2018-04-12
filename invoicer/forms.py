from django import forms

from .models import Ennery_ConfirmPOLines

class Ennery_ConfirmPOLinesf(forms.ModelForm):

    class Meta:
        model = Ennery_ConfirmPOLines
        fields = ('invoice', 'part', 'qty', 'value', 'po', 'eta', 'tlv')