from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from PIL import Image

# Create your models here.
class Tour(models.Model):
    """
    This model represents a Tour. An tour is anything you can buy
    tickets for.
    :param name: This event's full title
    :type name: str
    :param slug: A short, alphanumeric, all-lowercase name for use in URLs. The slug has to
                 be unique among the events of the same organizer.
    :type slug: str
    :param live: Whether or not the tour is publicly accessible
    :type live: bool
    :param date_from: The datetime this event starts
    :type date_from: datetime
    :param date_to: The datetime this event ends
    :type date_to: datetime
    :param location: venue
    :type location: str
    """

    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Tour name"
    )
    slug = models.SlugField(
        max_length=50, db_index=True,
        help_text=(
            "Should be short, only contain lowercase letters, numbers, dots, and dashes, and must be unique among your "
            "tours. You can also choose to use a random value. "
            "This will be used in URLs, order codes, invoice numbers, and bank transfer references."),
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9.-]+$",
                message=("The slug may only contain letters, numbers, dots and dashes."),
            )
        ],
        verbose_name="Short form"
    )
    tour_type = models.CharField(blank=True, max_length=100, help_text=(
        "Enter one of the following 'Walking', 'Cycling', 'Coach'"
        "Other tour types TBC"))
    tour_style = models.CharField(blank=True, max_length=100, help_text=(
        "Enter one of the following 'Street Food', 'Comfort Food', 'Izakaya food & Drink'"
        "Other tour styles TBC"))
    description = models.TextField(blank=True, max_length=400)
    city = models.CharField(blank=True, max_length=100)
    live = models.BooleanField(default=False, verbose_name="Tour is live")
    currency = models.CharField(max_length=3,
                                verbose_name="Tour currency",help_text=(
                                    "Enter the three letter currency code 'YEN'"))
    time_from = models.TimeField(verbose_name="Tour start time")
    time_to = models.TimeField(null=True, blank=True,
                                   verbose_name="Tour end time")
    start_location = models.TextField(
        null=True, blank=True,
        max_length=200,
        verbose_name="Start Location"
    )
    start_location_link = models.URLField(max_length=200)
    start_location_image = models.ImageField(upload_to ='static/images/location/',null=True, blank=True)
    end_location_link = models.URLField(max_length=200)
    tour_places = models.SmallIntegerField(blank=True, null=True)
    rating_culture = models.SmallIntegerField(blank=True, null=True)
    rating_fooddrink = models.SmallIntegerField(blank=True, null=True)
    rating_adventure = models.SmallIntegerField(blank=True, null=True)
    vegetarian_option = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    walking_distance = models.DecimalField(max_digits=3, decimal_places=1)


    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"

    def __str__(self):
        return str(self.name)
