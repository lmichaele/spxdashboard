from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Request(models.Model): #part, qty, WH, User, Date
    part_number = models.CharField(max_length=30)
    qty = models.IntegerField(default=0)
    WH = models.CharField(max_length=3) #change to checkboxes/radiobuttons to save multiple lines w same part for different warehosues
    User = models.CharField(max_length=10)
    Date = models.DateTimeField('date entered')
    def __str__(self):
        return self.part_number
    

# Create your models here.
