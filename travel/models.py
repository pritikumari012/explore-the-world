from django.db import models


class GFG(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()

    # Hotel information
    location = models.CharField(max_length=150, default="Unknown")
    rating = models.FloatField(default=4.0)
    hotel_image = models.URLField(blank=True)
    
    limited_time_offer = models.BooleanField(default=False)
    discount_percentage = models.IntegerField(default=0)

    # Facilities
    swimming_pool = models.BooleanField(default=False)
    internet = models.BooleanField(default=True)
    car_parking = models.BooleanField(default=False)
    airport_transfer = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)

    # Room information
    bedrooms = models.IntegerField(default=1)
    bed_type = models.CharField(max_length=50, default="Double Bed")

    # Property type
    property_type = models.CharField(
        max_length=50,
        default="Hotel"
    )

    # Dining
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)

    # Location coordinates - useful for distance-based sorting later
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.hotel_name