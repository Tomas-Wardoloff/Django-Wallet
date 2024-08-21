from django.utils.timezone import now
from django_filters import rest_framework as filters

from .models import Category


class CategoryFilter(filters.FilterSet):
    type = filters.CharFilter(field_name='type', lookup_expr='iexact')

    class Meta:
        model = Category
        fields = ['type']
