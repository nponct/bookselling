from django_filters  import rest_framework as filters
from .models import Books

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    user = filters.CharFilter(lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')
    cats = CharFilterInFilter(field_name='cats__name', lookup_expr='in')
    publ_date = filters.RangeFilter()

    class Meta:
        model = Books
        fields = ['user', 'title', 'cats', 'publ_date']



