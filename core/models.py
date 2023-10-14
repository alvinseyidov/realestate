from django.db import models



class General(models.Model):
    site_title = models.CharField(max_length=256)
    meta_description = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    whatsapp_link = models.CharField(max_length=256)
    telegram_link = models.CharField(max_length=256)
    copyright = models.CharField(max_length=256)
    logo = models.FileField()

    class Meta:
        verbose_name = "Ümumi Məlumatlar"
        verbose_name_plural = "Ümumi Məlumatlar"


    def __str__(self):
        return f'Ümumi Məlumatlar'


class Social(models.Model):
    link = models.CharField(max_length=256)
    icon = models.ImageField()
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Sosial Media Hesabı"
        verbose_name_plural = "Sosial Media Hesabları"

    def __str__(self):
        return self.name



class Why(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Why Alanya"
        verbose_name_plural = "Why Alanya"

    def __str__(self):
        return self.title

class AdvisorContact(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Advisora müraicət"
        verbose_name_plural = "Advisora müraicətlər"

    def __str__(self):
        return f'{self.name} {self.surname}'



class Tablar(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField()
    text = models.CharField(max_length=256)
    icon = models.FileField()

    class Meta:
        verbose_name = "Tablar"
        verbose_name_plural = "Tablar"

    def __str__(self):
        return self.title