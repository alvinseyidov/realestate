from django.db import models


class Offer(models.Model):
    name = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    bed = models.CharField(max_length=256)
    bath = models.CharField(max_length=256)
    square = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return self.name