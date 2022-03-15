from django.contrib import admin

from radientapp.models import Inquiry, Smallinq
from django.contrib import admin

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('firstname','middlename','lastname')
    search_fields= ('firstname','lastname',)

# Register your models here.
admin.site.register(Inquiry,InquiryAdmin)
admin.site.register(Smallinq)