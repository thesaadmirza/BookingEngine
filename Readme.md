# Django & Django REST framework test project.
The test project won't be used in any real environment.


## Summary:

Create DJANGO Project with DJANGO REST framework for:
- the main listing object could be a single unit (Apartment) or a multi-unit (Hotel)
    - single unit have booking information (price) directly connected to it.
    - multi units have booking information (price) connected to each of the children.
- filtering through Hotels/Apartments that returns JSON response with available units based on search criteria.
- the solution should be able to handle large dataset of units.

1. There is pre-build structure for Hotels/Apartments (could be changed/extended). With prefilled database.
    - superuser
        - username: **admin**
        - password: **admin**

2. We should be able to block days (already booked days) for each Apartment or HotelRoomType.
    - new Model for BlockedDays is needed

3. We need endpoint where we will get available Apartments and Hotels based on:
	- date range ( from 2021-12-09 to 2021-12-12) and max_price (100):
		- Apartment should not have any blocked day inside the range and should have price lower than max_price.
		- Hotel should have at least 1 Hotel Room without any blocked days in the range with price lower than max_price.

	- returned objects should be SORTED from lowest to highest price.
		- for hotels we should use the lowest AVAILABLE room_type price.


## Initial Project setup
    git clone https://bitbucket.org/staykeepersdev/bookingengine.git
    python -m venv venv
    pip install -r requirements.txt
    python manage.py runserver


## Test Case example:

For covering more test cases we are going to need at least one hotel with 3 Hotel Room Types:

- First with price=50 (below max_price) with blocked day inside the search criteria for all rooms(could be 1 room)

- Second with price=60 (below max_price) with blocked day insde the search criteria for one out of few rooms

- Third with price 200 (above max_price) 


## Request example:

http://localhost:8000/api/v1/units/?max_price=100&check_in=2021-12-09&check_out=2021-12-12


## Response example:

    {
        "items": [
            {
                "listing_type": "Apartment",
                "title": "Luxurious Studio",
                "country": "UK",
                "city": "London",
                "price": "40"

            },
            {
                "listing_type": "Hotel",
                "title": "Hotel Lux 3***",
                "country": "BG",
                "city": "Sofia",
                "price": "60" # This the price of the first Hotel Room Type with a Room without blocked days in the range

            },
            {
                "listing_type": "Apartment",
                "title": "Excellent 2 Bed Apartment Near Tower Bridge",
                "country": "UK",
                "city": "London",
                "price": "90"
            },
        ]
    }