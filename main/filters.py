import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    start_pay = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    stop_pay = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
