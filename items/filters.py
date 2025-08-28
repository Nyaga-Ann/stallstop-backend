import django_filters
from .models import Item

class ItemFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    vendor_location = django_filters.CharFilter(field_name="vendor__location", lookup_expr="icontains")

    class Meta:
        model = Item
        fields = ["category", "vendor_location", "min_price", "max_price"]
s