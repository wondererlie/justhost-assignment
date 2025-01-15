from django_filters import rest_framework as filters

from vps.models import VPS


class VPSFilter(filters.FilterSet):
    class Meta:
        model = VPS
        fields = {
            'cpu': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'ram': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'hdd': ['exact', 'lt', 'lte', 'gt', 'gte'],
        }
