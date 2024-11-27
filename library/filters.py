from django_filters.rest_framework import FilterSet, BooleanFilter

from .models import Book


class BookFilter(FilterSet):
    availability_status = BooleanFilter(method='filter_availability_status', label='Availability Status')
    
    class Meta:
        model = Book
        fields = {
            'author_id': ['exact'],
            'tag': ['exact'],
                }
        
    def filter_availability_status(self, queryset, name, value):
        if value:  # True: Only available books
            return queryset.exclude(borrow__status='borrowed')
        else:  # False: Only unavailable books
            return queryset.filter(borrow__status='borrowed')
