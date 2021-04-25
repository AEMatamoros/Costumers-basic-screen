import django_filters
from django import forms
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date_created',lookup_expr='gte',widget=forms.TextInput(attrs={'type':'date'}))
    end_date = django_filters.DateFilter(field_name='date_created',lookup_expr='lte',widget=forms.TextInput(attrs={'type':'date'}))
    note = django_filters.CharFilter(field_name='note', lookup_expr="contains",widget=forms.TextInput(attrs={'class':'form form-control'}))
    class Meta:
        model = Order
        fields = {
            'product',
            'status',
            
        }
        exlude = ['costumer','date_created']

