from django.contrib import admin
from .models import Members, MembersAdmin, DateActive
# Register your models here.

admin.site.site_header = "Felinfach On-Call Rota"
admin.site.site_title =  "Felinfach On-Call Rota"
admin.site.index_title = "Felinfach On-Call Rota"



def change_status_active(modeladmin, request, queryset):
    queryset.update(isactive=1)
change_status_active.short_description = 'Change Date - Active'

def change_status_inactive(modeladmin, request, queryset):
    queryset.update(isactive=0)
change_status_inactive.short_description = 'Change Date - Inactive'

def DayCount(obj):
    days = obj.startdate - obj.enddate
    return days 
class DateActiveadmin(admin.ModelAdmin):

    fieldsets = [
        ('Rota Schedule',{'fields':['isactive','startdate','enddate','employee',]}),

    ]
    list_display = ('startdate','enddate','employee','isactive', DayCount)
    #list_editable = ('isactive',)
    list_filter = ('startdate','enddate','employee','isactive')
    ordering = ('startdate',)
    actions = [change_status_active,change_status_inactive,]




admin.site.register(Members,MembersAdmin)
admin.site.register(DateActive, DateActiveadmin)

