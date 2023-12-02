from django.db import models


class Offer(models.Model):
    TYPE = (
        ('V', 'Villa'),
        ('A', 'Apartment'),
    )
    name = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    project_status = models.CharField(max_length=256)
    year_built = models.CharField(max_length=256)
    distance_to_beach = models.CharField(max_length=256)
    distance_to_center = models.CharField(max_length=256)
    distance_to_airport = models.CharField(max_length=256)
    state_guaranteed = models.CharField(max_length=256)
    sea_view = models.CharField(max_length=256)
    installment = models.CharField(max_length=256)
    suitable_for_citizenship = models.CharField(max_length=256)
    bed = models.CharField(max_length=256)
    bath = models.CharField(max_length=256)
    square = models.CharField(max_length=256)
    type = models.CharField(max_length=1, choices=TYPE, default='V')
    image = models.ImageField()

    sanitaires = models.CharField(max_length=256, default='2')
    balcon = models.CharField(max_length=256, default='2')
    rooms = models.CharField(max_length=256, default='2')
    chambres = models.CharField(max_length=256, default='2')
    wc_qty = models.CharField(max_length=256, default='2')
    indoor_parking = models.CharField(max_length=256, default='1')
    heating_system = models.CharField(max_length=256, default='Floor')

    description = models.TextField()

    ilkin_mebleg = models.CharField(max_length=256, null=True,blank=True)
    maks_ayliq_kiraye = models.CharField(max_length=256, null=True,blank=True)
    real_bazar_qiymeti = models.CharField(max_length=256, null=True,blank=True)
    umumi_mebleg = models.CharField(max_length=256, null=True,blank=True)
    on_il_sonraki_qiymet = models.CharField(max_length=256, null=True,blank=True)
    umumi_net_gelir = models.CharField(max_length=256, null=True,blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()

    def __str__(self):
        return f'şəkil'