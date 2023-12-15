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
    home_popup_video = models.FileField()
    countdown_enddate = models.DateTimeField()

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



class Feedback(models.Model):
    user_image = models.ImageField()
    full_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    text = models.TextField()
    background_image = models.ImageField()

    def __str__(self):
        return self.full_name


class Why(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Why Alanya"
        verbose_name_plural = "Why Alanya"

    def __str__(self):
        return self.title





class Tablar(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField()
    text = models.CharField(max_length=256, null=True, blank=True)
    icon = models.FileField()

    class Meta:
        verbose_name = "Tablar"
        verbose_name_plural = "Tablar"

    def __str__(self):
        return self.title



class FAQ(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=256)
    sort = models.IntegerField()

    class Meta:
        ordering = ('sort',)

    def __str__(self):
        return self.question




class Feature(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    icon = models.FileField()
    description = models.TextField()
    color = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Waitlist(models.Model):
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} {self.email} - {self.phone}'