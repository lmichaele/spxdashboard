from django.contrib import admin
from import_export import resources
from .models import Request

class PartsResource(resources.ModelResource):

	class Meta:
		model = Request
		fields = ('part_number', 'qty', 'WH', 'OTP')

admin.site.register(Request)
