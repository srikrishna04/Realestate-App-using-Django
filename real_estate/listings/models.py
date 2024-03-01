from django.db import models

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_halls = models.IntegerField()
    Square_footage = models.IntegerField()
    Address = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title

