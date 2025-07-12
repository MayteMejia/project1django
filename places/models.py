from django.db import models
from .validators import validate_rating, validate_price_positive

class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Ubication(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    link_maps = models.CharField(max_length=500, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.city

class PriorityPlace(models.TextChoices):
    HIGH = 'H', 'High'
    MEDIUM = 'M', 'Medium'
    LOW = 'L', 'Low'

class Place(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    ubication = models.ForeignKey(Ubication, on_delete=models.CASCADE)
    price_aprox = models.DecimalField(decimal_places=2, max_digits=10, validators=[validate_price_positive,], null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    priority = models.CharField(
        choices = PriorityPlace.choices,
        default=PriorityPlace.LOW
    )
    visited = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Schedule(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='schedule')
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Visit(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateField()
    coment = models.TextField(null=True, blank=True)
    rating = models.IntegerField(validators=[validate_rating,])