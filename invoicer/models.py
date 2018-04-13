from django.db import models

# Create your models here.

class Ennery_ConfirmPOLines(models.Model):  
    invoice = models.CharField(max_length=8, verbose_name="invoice")
    part = models.CharField(max_length=30, verbose_name="part")
    qty = models.IntegerField(verbose_name="qty")
    value = models.FloatField(max_length=8, verbose_name="value")
    po = models.CharField(max_length=20, verbose_name="po")
    eta = models.CharField(max_length=8, verbose_name="eta")
    tlv = models.CharField(max_length=20, verbose_name="tlv")

class Sparex_Invoice(models.Model):
    connection = models.CharField(max_length=10, verbose_name="connection")
    part = models.CharField(max_length=30, verbose_name="part")
    qty = models.IntegerField(verbose_name="qty")
    value = models.FloatField(max_length=30, verbose_name="value")
    po = models.CharField(max_length=20, verbose_name="po")
    eta = models.CharField(max_length=30, verbose_name="eta")
    #line = models.IntegerField(verbose_name="line")
    invoice = models.CharField(max_length=30, verbose_name="invoice")
    tlv = models.CharField(max_length=20, verbose_name="tlv")