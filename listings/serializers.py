from listings.models import BookingInfo, Listing
from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    price = serializers.SlugRelatedField(
        source='booking_info',
        slug_field='price',
        read_only=True,
    )
    
    class Meta:
        model = Listing
        fields = ['listing_type', 'title', 'country', 'city', 'price']
