from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from .models import Members, MembersAdmin, DateActive
from datetime import datetime
# Register your models here.

admin.site.site_header = "On-Call Rota"
admin.site.site_title =  "On-Call Rota"
admin.site.index_title = "On-Call Rota"



def change_status_active(modeladmin, request, queryset):
    queryset.update(isactive=1)
change_status_active.short_description = 'Change Date - Active'

def change_status_inactive(modeladmin, request, queryset):
    queryset.update(isactive=0)
change_status_inactive.short_description = 'Change Date - Inactive'

def DayCount(obj):
    days = obj.enddate - obj.startdate
    return days

    


class DateActiveadmin(admin.ModelAdmin):

    fieldsets = [
        ('Rota Schedule',{'fields':['isactive','startdate','enddate','employee',]}),

    ]
    list_display = ('startdate','enddate','employee','isactive', DayCount)
    #list_editable = ('isactive',)
    list_filter = ('startdate','enddate','employee','isactive')
    ordering = ('-startdate',)
    actions = [change_status_active,change_status_inactive,]

    def count_days(modeladmin, request, querset):
        today = datetime.date.today()
        first = today.replace(day=1)
        lastmonth = first - datetime.timedelta(days=1)

        DateActive.objects.filter(startdate=lastmonth)


admin.site.register(Members,MembersAdmin)
admin.site.register(DateActive, DateActiveadmin)

