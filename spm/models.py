from django.db import models
from datetime import datetime, timedelta
from django.contrib import admin
from django.core.validators import ValidationError


# Create your models here.

#def validate_digit_length(phone):
#    if not (phone.isdigit() and len(phone) == 11):    
#        raise ValidationError('%(phone)s must be 11 digits', params={'phone': phone},)
    #validators=[validate_digit_length])

class SiteLocation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(verbose_name="Phone Number", max_length=13)
    def __str__(self):
        return self.name


class Members(models.Model):
    firstname = models.CharField(max_length=250)
    surname   = models.CharField(max_length=250)
    email     = models.CharField(max_length=250)
    mobile    = models.CharField(verbose_name="Phone Number", max_length=13)
    class Meta:
        verbose_name = "Member"
    def __str__(self):
        return self.firstname + " " + self.surname

class DateActiveManager(models.Manager):
    def get_queryset(self):
        return super(DateActiveManager, self).get_queryset().filter(isactive='True')
class DateActive(models.Model):
    def default_start_time():
        now = datetime.now()
        start = now.replace(hour=7, minute=0, second=0, microsecond=0 )
        return start if start > now else start + timedelta(days=1)
    def default_end_time():
        now = datetime.now()
        end = now.replace(hour=6, minute=59, second=59, microsecond=0)
        return end if end > now else end + timedelta(days=1)
    isactive  = models.BooleanField(default=1)
    startdate = models.DateTimeField(max_length=250,default=default_start_time)
    enddate   = models.DateTimeField(max_length=250,default=default_end_time)
    employee  = models.ForeignKey(Members, on_delete=models.CASCADE)
    deskphone = models.ForeignKey(SiteLocation, on_delete=models.CASCADE, blank=True, default=1)
    objects = models.Manager()
    showactive = DateActiveManager()
    class Meta:
        verbose_name = "Active Date"
    def __str__(self):
        return str(self.startdate)



def full_name(obj):
    return '%s %s' % (obj.firstname, obj.surname)

class MembersAdmin(admin.ModelAdmin):
    list_display = (full_name , 'email', 'mobile')
