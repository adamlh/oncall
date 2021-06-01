from .models import DateActive
import django_filters

class DateActiveFilter(django_filters.FilterSet):
	
    class Meta:
        model = DateActive
        fields = [
            'startdate',
            'enddate',
            'employee',
        ]