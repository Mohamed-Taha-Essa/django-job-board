import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude=['slug','ownerr','published_at','salary']
       