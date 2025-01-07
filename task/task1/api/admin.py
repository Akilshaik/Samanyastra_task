from django.contrib import admin
from api.models import pepoles

# Register your models here.
class pepolesadmin(admin.ModelAdmin):
    list_display=('p_id','name','location')

admin.site.register(pepoles, pepolesadmin)