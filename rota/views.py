from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DateActive, Members, DateActiveManager
from django.http import HttpResponse
from django.utils import timezone
from calendar import monthrange

from datetime import datetime, timedelta, date
from .filters import DateActiveFilter

# Create your views here.


class RotaView(TemplateView):
    template_name = 'rota.html'
    def get(self, request):
        now = timezone.now()
        first_day_month = now.replace(day=1)
        last_day_month  = now.replace(day = monthrange(now.year, now.month)[1])
        #date_range = DateActive.objects.filter("2020-11-01","2020-11-29")
        adamtotaldays = DateActive.objects.filter(
            employee=1,).filter(
            startdate__month = now.month - 1,
            enddate__month = (now.month  - 1)
        )

        stefftotaldays = DateActive.objects.filter(
            employee=2,).filter(
            startdate__month = now.month - 1,
            enddate__month = (now.month  - 1)
        )

        kaltotaldays = DateActive.objects.filter(
            employee=4,).filter(
            startdate__month = now.month - 1,
            enddate__month = (now.month  - 1)
        )
        dates = DateActive.objects.filter(startdate__lte=now, enddate__gte=now)
        args = {'dates': dates, 'name': DateActive.employee, 'adamtotaldays': str(adamtotaldays.count()), 'steffandays': str(stefftotaldays.count()), 'kaldays': str(kaltotaldays.count())}
        return render(request, self.template_name, args)


class RotaTotalView(TemplateView):
    template_name = 'total.html'
    def get(self, request):
        today = date.today()
        first = today.replace(day=1)
        firstDayOfLastMonth = today.replace(day=1, month=today.month-1)
        lastDayOfLastMonth = first - timedelta(days=1)
        previous_month = str(firstDayOfLastMonth) + " " + str(lastDayOfLastMonth) 
        now = date.today()
        query = DateActive.objects.all().date_range=['2020','11','01',]

        adamtotaldays = DateActive.objects.all().filter(employee=1, startdate__year=firstDayOfLastMonth.year, startdate__month=firstDayOfLastMonth.month, enddate__year=lastDayOfLastMonth.year, enddate__month=lastDayOfLastMonth.month)
        stefftotaldays = DateActive.objects.all().filter(employee=2, startdate__year=firstDayOfLastMonth.year, startdate__month=firstDayOfLastMonth.month, enddate__year=lastDayOfLastMonth.year, enddate__month=lastDayOfLastMonth.month)
        kaltotaldays = DateActive.objects.all().filter(employee=4, startdate__year=firstDayOfLastMonth.year, startdate__month=firstDayOfLastMonth.month, enddate__year=lastDayOfLastMonth.year, enddate__month=lastDayOfLastMonth.month)
        dates = DateActive.objects.filter(startdate__lte=now, enddate__gte=now)
        args = {'dates': dates, 'name': DateActive.employee, 'adamtotaldays': str(adamtotaldays.count()*7), 'steffandays': str(stefftotaldays.count()*7), 'kaldays': str(kaltotaldays.count()*7), "previous_month" : previous_month}
        return render(request, self.template_name, args)
        
        
def search(request):     
    date_list = DateActive.objects.all()
    date_filter = DateActiveFilter(request.GET, queryset=date_list)
    return render(request, 'search/date_list.html', {'filter': date_filter})
    
        