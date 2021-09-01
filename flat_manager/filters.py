import django_filters

from .models import *

class FlatFilter(django_filters.FilterSet):
    class Meta:
        model = Flat
        fields = ['city', 'street']
        # exclude = ['flat_surface', ]

