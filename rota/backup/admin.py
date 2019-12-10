from django.contrib import admin
from .models import Members, MembersAdmin, DateActive, DateActiveadmin
# Register your models here.

admin.site.site_header = "Felinfach On-Call Rota"
admin.site.site_title =  "Felinfach On-Call Rota"
admin.site.index_title = "Felinfach On-Call Rota"

admin.site.register(Members,MembersAdmin)
admin.site.register(DateActive, DateActiveadmin)