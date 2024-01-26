from django.db import models


class Offer(models.Model):
    TYPE = (
        ('V', 'Villa'),
        ('M', 'Mənzil'),
        ('E', 'Ev'),
        ('T', 'Torpaq'),
        ('Q', 'Qeyri-yaşayış'),
        ('B', 'Bina'),
    )
    price = models.IntegerField(verbose_name="Əmlakın Indiki Dəyəri",default=0)
    ilkin_kapital = models.IntegerField(verbose_name="İlkin kapital",null=True, blank=True)
    kiraye_geliri = models.IntegerField(verbose_name="Ortalama Kirayə Gəliri",null=True, blank=True)
    emlakın_deyeri = models.IntegerField(verbose_name="Əmlakın 10 İl Sonrakı Dəyəri",null=True, blank=True)
    net_qazanc = models.IntegerField(verbose_name="Net Qazanc",null=True, blank=True)
    kirayeci = models.CharField(verbose_name="Kirayəçi Yerləşdirmə",max_length=256)
    name = models.CharField(max_length=256)
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

    class Meta:
        verbose_name = "Ev, Villa"
        verbose_name_plural = "Evlər, Villalar"
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # set the value of the read_only_field using the regular field
        if not self.ilkin_kapital:
            self.ilkin_kapital = self.price * 0.6
        import requests
        response = requests.get("https://smartinvest.az/data/10/"+ str(int(self.ilkin_kapital))+"/1")
        print(response.json()['kiraye'])

        if not self.kiraye_geliri:
            self.kiraye_geliri = response.json()['kiraye']/10
        if not self.emlakın_deyeri:
            self.emlakın_deyeri = response.json()['deyer']
        if not self.net_qazanc:
            self.net_qazanc = response.json()['yatirim_qazanci_tr'][9]

        # call the save() method of the parent
        super(Offer, self).save(*args, **kwargs)


class Image(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()

    def __str__(self):
        return f'şəkil'


class Message(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    message = models.TextField()

    class Meta:
        verbose_name = "Ev, Villa Müraciət Edən"
        verbose_name_plural = "Evlər, Villalar  Müraciət Edənlər"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'