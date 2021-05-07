from django.contrib import admin

# Register your models here.
from .models import StationsNew, MonthNew

admin.site.register(StationsNew)
admin.site.register(MonthNew)
