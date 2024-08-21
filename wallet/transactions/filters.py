from django.utils.timezone import now
from django_filters import rest_framework as filters

from datetime import timedelta

from .models import Transaction


class TransactionFilter(filters.FilterSet):
    type = filters.CharFilter(
        field_name='category__type', lookup_expr='iexact')
    last_week = filters.BooleanFilter(method='filter_last_week')
    last_month = filters.BooleanFilter(method='filter_last_month')
    last_3_months = filters.BooleanFilter(method='filter_last_3_months')

    class Meta:
        model = Transaction
        fields = ['type', 'last_week', 'last_month', 'last_3_months']

    def filter_last_week(self, queryset, name, value):
        if value:
            start_date = now() - timedelta(days=7)
            return queryset.filter(date__gte=start_date)
        return queryset

    def filter_last_month(self, queryset, name, value):
        if value:
            start_date = now() - timedelta(days=30)
            return queryset.filter(date__gte=start_date)
        return queryset

    def filter_last_3_months(self, queryset, name, value):
        if value:
            start_date = now() - timedelta(days=90)
            return queryset.filter(date__gte=start_date)
        return queryset
