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
        verbose_name = "Ümumi Sayt Məlumatlar"
        verbose_name_plural = "Ümumi Sayt Məlumatlar"


    def __str__(self):
        return f'Ümumi Sayt Məlumatlar'


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

    class Meta:
        verbose_name = "Müştəri Geri Bildirim"
        verbose_name_plural = "Müştəri Geri Bildirimləri"

    def __str__(self):
        return self.full_name


class Why(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Komanda üzvü"
        verbose_name_plural = "Komanda"

    def __str__(self):
        return self.title

class Head(models.Model):
    name = models.CharField(max_length=256)
    script = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "   Head'ə əlavə olunan scriptlər"
        verbose_name_plural = "   Head'ə əlavə olunan scriptlər"


class Body(models.Model):
    WHERE = (
        ('H','Script in between HEAD tags'),
        ('T','After <body> tag opened'),
        ('B','Before </body> tag closed'),
    )
    name = models.CharField(max_length=256)
    script = models.TextField()
    location = models.CharField(choices=WHERE, max_length=1, default='T')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "  JS Script"
        verbose_name_plural = "  JS Scriptlər"

class Parametr(models.Model):
    leverage_tr = models.DecimalField(verbose_name='Leverage TR',max_digits=8, decimal_places=5)
    leverage_az = models.DecimalField(verbose_name='Leverage AZ',max_digits=8, decimal_places=5)
    loan_interest_rate_tr = models.DecimalField(verbose_name='Loan Interest Rate TR',max_digits=8, decimal_places=5)
    loan_interest_rate_az = models.DecimalField(verbose_name='Loan Interest Rate AZ',max_digits=8, decimal_places=5)
    appraisal_rate_tr = models.DecimalField(verbose_name='Appraisal Rate TR',max_digits=8, decimal_places=5)
    appraisal_rate_az = models.DecimalField(verbose_name='Appraisal Rate AZ',max_digits=8, decimal_places=5)
    rental_growth_tr = models.DecimalField(verbose_name='Rental Growth TR',max_digits=8, decimal_places=5)
    rental_growth_az = models.DecimalField(verbose_name='Rental Growth AZ',max_digits=8, decimal_places=5)
    interest_rate_tr = models.DecimalField(verbose_name='Interest Rate TR',max_digits=8, decimal_places=5)
    interest_rate_az = models.DecimalField(verbose_name='Interest Rate AZ',max_digits=8, decimal_places=5)
    diger_xercler_tr = models.DecimalField(verbose_name='Digər Xərclər TR',max_digits=8, decimal_places=1)
    diger_xercler_az = models.DecimalField(verbose_name='Digər Xərclər AZ',max_digits=8, decimal_places=1)
    heyat_sigortasi_tr = models.DecimalField(verbose_name='Həyat Siğortası TR',max_digits=8, decimal_places=1)
    heyat_sigortasi_az = models.DecimalField(verbose_name='Həyat Siğortası AZ',max_digits=8, decimal_places=1)
    kiraye_kofisent_tr = models.DecimalField(verbose_name='Kirayə Gəliri Kofisenti TR',max_digits=8, decimal_places=5)
    kiraye_kofisent_az = models.DecimalField(verbose_name='Kirayə Gəliri Kofisenti AZ',max_digits=8, decimal_places=5)

    class Meta:
        verbose_name = "Kalkulyator Parametrləri"
        verbose_name_plural = "Kalkulyator Parametrləri"

    def __str__(self):
        return f'Kalkulyator Parametrləri'



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
        verbose_name = "FAQ Sual"
        verbose_name_plural = "FAQ Suallar"

    def __str__(self):
        return self.question




class Feature(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    icon = models.FileField()
    description = models.TextField()
    color = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Niyə? Səbəblər"
        verbose_name_plural = "Niyə? Səbəblər"

    def __str__(self):
        return self.title

