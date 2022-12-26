from django.contrib import admin
from .models import Bio,Event1,Event2,Dept,Workshop,WorkshopBio
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class FilterAdmin(ImportExportModelAdmin):
    list_display = ("__str__",'institute',"dept","abstract","razorpay_payment_id")
    list_filter = ("event2","event1","institute","dept","iitg_student")
    search_fields = ('institute',)

class WorkshopAdmin(ImportExportModelAdmin):
    list_display = ('__str__','dept','razorpay_payment_id')
    list_filter = ("workshop",)



admin.site.register(Bio,FilterAdmin)
admin.site.register(Event1)
admin.site.register(Event2)
admin.site.register(Dept)
admin.site.register(Workshop)
admin.site.register(WorkshopBio,WorkshopAdmin)
