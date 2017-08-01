from django import forms

from .models import Request

class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ('part_number', 'qty', 'WH',)
                
