from listings.models import Listing
from django.utils.dateparse import parse_date
from listings.serializers import ListingSerializer
from rest_framework import generics
from listings.pagination import StandardResultsSetPagination


# Create your views here.
class ListApiView(generics.ListAPIView):
    queryset = Listing.objects.all().order_by('booking_info__price')
    serializer_class = ListingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned Listing to Max Price and Date Ranges
        """
        queryset = Listing.objects.all().order_by('booking_info__price')
        max_price = self.request.query_params.get('max_price')
        if max_price is not None:
            queryset = queryset.filter(booking_info__price__lte=max_price)

        # Date Range of Check and Check Out
        check_in = self.request.query_params.get('check_in')
        check_out = self.request.query_params.get('check_out')
        if check_in is not None and check_out is not None:
            check_in = parse_date(check_in)
            check_out = parse_date(check_out)
            queryset = queryset.exclude(hotel_room_types__blocked_days__day__gte=check_in,
                                        hotel_room_types__blocked_days__day__lte=check_out)

        return queryset
