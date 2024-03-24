from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Car (models.Model):
    car_id =  models.AutoField(primary_key=True)
    car_name = models.TextField(max_length=255)
    car_year = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )