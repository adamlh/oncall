from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DateActive, Members, DateActiveManager
from django.http import HttpResponse
from datetime import date
from django.utils import timezone
# Create your views here.


class SpmView(TemplateView):
    template_name = 'spm.html'
    def get(self, request):
        now = timezone.now()
        dates = DateActive.objects.filter(startdate__lte=now, enddate__gte=now)
        members = Members.objects.all()
        args = {'dates': dates, 'name': DateActive.employee, 'members':members}
        return render(request, self.template_name, args)

# Create your views here.
