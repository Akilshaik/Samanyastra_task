from django.contrib import admin
from apps.firstapp.models import Person

# Register your models here.

class personadmin(admin.ModelAdmin):
    list_display=('first_name','last_name')

admin.site.register(Person, personadmin)