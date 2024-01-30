from django.db import models

# Create xyour models here.
class Waitlist(models.Model):
    email = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Gözləmədə Olan"
        verbose_name_plural = "Gözləmədə Olanlar"

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    prefix = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Əlaqə Formu Müraciət"
        verbose_name_plural = "Əlaqə Formu Müraciətlər"

    def __str__(self):
        return f'{self.name} {self.email} - {self.phone}'



class Vebinar(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    prefix = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Vebinar Müraciət"
        verbose_name_plural = "Vebinar Müraciətlər"

    def __str__(self):
        return f'{self.first_name} {self.email} - {self.phone}'