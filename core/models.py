from django.db import models


class VebinarForm(models.Model):
    label = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    placeholder = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)
        verbose_name = "Dynamic Vebinar Form"
        verbose_name_plural = "Dynamic Vebinar Form"
    def __str__(self):
        return self.label


class MenzilForm(models.Model):
    label = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    placeholder = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)
        verbose_name = "Dynamic Menzil Form  "
        verbose_name_plural = "Dynamic Menzil Form  "
    def __str__(self):
        return self.label



class VebinarFormTR(models.Model):
    label = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    placeholder = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)
        verbose_name = "Dynamic Vebinar Form TR"
        verbose_name_plural = "Dynamic Vebinar Form TR"
    def __str__(self):
        return self.label


class MenzilFormTR(models.Model):
    label = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    placeholder = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)
        verbose_name = "Dynamic Menzil Form TR"
        verbose_name_plural = "Dynamic Menzil Form TR"
    def __str__(self):
        return self.label



class VebinarFormRU(models.Model):
    label = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    placeholder = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)
        verbose_name = "Dynamic Vebinar Form RU"
        verbose_name_plural = "Dynamic Vebinar Form RU"
    def __str__(self):
        return self.label


class MenzilFormRU(models.Model):
    label = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    placeholder = models.CharField(max_length=256)
    sort = models.IntegerField(default=0)
    class Meta:
        ordering = ('sort',)
        verbose_name = "Dynamic Menzil Form RU"
        verbose_name_plural = "Dynamic Menzil Form RU"
    def __str__(self):
        return self.label
class Slider(models.Model):
    color = (
        ('B','black'),
        ('W','white'),
    )
    background_image = models.ImageField()
    title = models.CharField(max_length=256)
    mobile_title = models.CharField(max_length=256,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    button_text = models.CharField(max_length=256,null=True, blank=True)
    button_url = models.CharField(max_length=256,null=True, blank=True)
    button_color = models.CharField(max_length=1,default='W',choices=color)
    button_text_color = models.CharField(max_length=1,default='B',choices=color)
    image_link = models.CharField(max_length=256,null=True, blank=True)
    sorting = models.IntegerField(default=1)
    black_layer_css = models.CharField(max_length=256,default="background: linear-gradient(90deg, #000 33.33%, rgba(0, 0, 0, 0.00) 99.89%)",null=True, blank=True)
    black_layer_css_mobile = models.CharField(max_length=256,default="background: linear-gradient(180deg, #000 33.33%, rgba(0, 0, 0, 0.00) 99.89%)",null=True, blank=True)



    class Meta:
        ordering = ('sorting',)

    def __str__(self):
        return self.title


class SliderTR(models.Model):
    color = (
        ('B','black'),
        ('W','white'),
    )
    background_image = models.ImageField()
    title = models.CharField(max_length=256)
    mobile_title = models.CharField(max_length=256,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    button_text = models.CharField(max_length=256,null=True, blank=True)
    button_url = models.CharField(max_length=256,null=True, blank=True)
    button_color = models.CharField(max_length=1,default='W',choices=color)
    button_text_color = models.CharField(max_length=1,default='B',choices=color)
    image_link = models.CharField(max_length=256,null=True, blank=True)
    sorting = models.IntegerField(default=1)
    black_layer_css = models.CharField(max_length=256,default="background: linear-gradient(90deg, #000 33.33%, rgba(0, 0, 0, 0.00) 99.89%)",null=True, blank=True)
    black_layer_css_mobile = models.CharField(max_length=256,default="background: linear-gradient(180deg, #000 33.33%, rgba(0, 0, 0, 0.00) 99.89%)",null=True, blank=True)



    class Meta:
        ordering = ('sorting',)
        verbose_name = "Tr Slider"
        verbose_name_plural = "Tr Slider"

    def __str__(self):
        return self.title

class General(models.Model):
    site_title = models.CharField(max_length=256)
    favicon = models.FileField()
    meta_description = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    whatsapp_link = models.CharField(max_length=256)
    telegram_link = models.CharField(max_length=256)
    copyright = models.CharField(max_length=256)
    logo = models.FileField()
    logo_white = models.FileField(null=True, blank=True)
    home_popup_video = models.FileField(null=True, blank=True)
    countdown_enddate = models.DateTimeField(null=True, blank=True)

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


class FeedbackTR(models.Model):
    user_image = models.ImageField()
    full_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    text = models.TextField()
    background_image = models.ImageField()

    class Meta:
        verbose_name = "Tr Müştəri Geri Bildirim"
        verbose_name_plural = "Tr Müştəri Geri Bildirimləri"

    def __str__(self):
        return self.full_name

class Why(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    position = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Komanda üzvü"
        verbose_name_plural = "Komanda"

    def __str__(self):
        return self.title

class CalendlyScript(models.Model):
    name = models.CharField(max_length=256)
    script = models.TextField()

    def __str__(self):
        return self.name

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
    title = models.CharField(verbose_name='Bölmənin başlığı',max_length=256)
    leverage_tr = models.FloatField(verbose_name='Leverage Percent TR')
    leverage_az = models.FloatField(verbose_name='Leverage Percent AZ')
    loan_interest_rate_tr = models.FloatField(verbose_name='Loan Interest Rate TR')
    loan_interest_rate_az = models.FloatField(verbose_name='Loan Interest Rate AZ')
    interest_rate_bank = models.FloatField(verbose_name='Bank Interest Rate AZ')
    appraisal_rate_tr = models.FloatField(verbose_name='Appraisal Rate TR')
    appraisal_rate_az = models.FloatField(verbose_name='Appraisal Rate AZ')
    rental_growth_tr = models.FloatField(verbose_name='Rental Growth TR')
    rental_growth_az = models.FloatField(verbose_name='Rental Growth AZ')
    diger_xercler_tr = models.FloatField(verbose_name='Digər Xərclər TR')
    diger_xercler_az = models.FloatField(verbose_name='Digər Xərclər AZ')
    heyat_sigortasi_tr = models.FloatField(verbose_name='Həyat Siğortası TR')
    heyat_sigortasi_az = models.FloatField(verbose_name='Həyat Siğortası AZ')
    kiraye_kofisent_tr = models.FloatField(verbose_name='Kirayə Gəliri Kofisenti TR')
    kiraye_kofisent_az = models.FloatField(verbose_name='Kirayə Gəliri Kofisenti AZ')

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
    answer = models.CharField(max_length=512)
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


class SliderRU(models.Model):
    color = (
        ('B', 'black'),
        ('W', 'white'),
    )
    background_image = models.ImageField()
    title = models.CharField(max_length=256)
    mobile_title = models.CharField(max_length=256, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    button_text = models.CharField(max_length=256, null=True, blank=True)
    button_url = models.CharField(max_length=256, null=True, blank=True)
    button_color = models.CharField(max_length=1, default='W', choices=color)
    button_text_color = models.CharField(max_length=1, default='B', choices=color)
    image_link = models.CharField(max_length=256, null=True, blank=True)
    sorting = models.IntegerField(default=1)
    black_layer_css = models.CharField(max_length=256,
                                       default="background: linear-gradient(90deg, #000 33.33%, rgba(0, 0, 0, 0.00) 99.89%)",
                                       null=True, blank=True)
    black_layer_css_mobile = models.CharField(max_length=256,
                                              default="background: linear-gradient(180deg, #000 33.33%, rgba(0, 0, 0, 0.00) 99.89%)",
                                              null=True, blank=True)

    class Meta:
        ordering = ('sorting',)
        verbose_name = "Ru Slider"
        verbose_name_plural = "Ru Slider"

    def __str__(self):
        return self.title


class GeneralRU(models.Model):
    site_title = models.CharField(max_length=256)
    favicon = models.FileField()
    meta_description = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    whatsapp_link = models.CharField(max_length=256)
    telegram_link = models.CharField(max_length=256)
    copyright = models.CharField(max_length=256)
    logo = models.FileField()
    logo_white = models.FileField(null=True, blank=True)
    home_popup_video = models.FileField(null=True, blank=True)
    countdown_enddate = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Ümumi Sayt Məlumatlar"
        verbose_name_plural = "Ru Ümumi Sayt Məlumatlar"

    def __str__(self):
        return f'Ümumi Sayt Məlumatlar'


class FeedbackRU(models.Model):
    user_image = models.ImageField()
    full_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    text = models.TextField()
    background_image = models.ImageField()

    class Meta:
        verbose_name = "Ru Müştəri Geri Bildirim"
        verbose_name_plural = "Ru Müştəri Geri Bildirimləri"

    def __str__(self):
        return self.full_name


class WhyRU(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    position = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Komanda üzvü"
        verbose_name_plural = "Ru Komanda"

    def __str__(self):
        return self.title


class FAQRU(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=512)
    sort = models.IntegerField()

    class Meta:
        ordering = ('sort',)
        verbose_name = "FAQ Sual"
        verbose_name_plural = "RU FAQ Suallar"

    def __str__(self):
        return self.question


class FeatureRU(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    icon = models.FileField()
    description = models.TextField()
    color = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Niyə? Səbəblər"
        verbose_name_plural = "RU Niyə? Səbəblər"

    def __str__(self):
        return self.title

class FeatureTR(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    icon = models.FileField()
    description = models.TextField()
    color = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Niyə? Səbəblər"
        verbose_name_plural = "Tr Niyə? Səbəblər"

    def __str__(self):
        return self.title






class GeneralTR(models.Model):
    site_title = models.CharField(max_length=256)
    favicon = models.FileField()
    meta_description = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    whatsapp_link = models.CharField(max_length=256)
    telegram_link = models.CharField(max_length=256)
    copyright = models.CharField(max_length=256)
    logo = models.FileField()
    logo_white = models.FileField(null=True, blank=True)
    home_popup_video = models.FileField(null=True, blank=True)
    countdown_enddate = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Ümumi Sayt Məlumatlar"
        verbose_name_plural = "Tr Ümumi Sayt Məlumatlar"

    def __str__(self):
        return f'Ümumi Sayt Məlumatlar'





class WhyTR(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    position = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Komanda üzvü"
        verbose_name_plural = "Tr Komanda"

    def __str__(self):
        return self.title


class FAQTR(models.Model):
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=512)
    sort = models.IntegerField()

    class Meta:
        ordering = ('sort',)
        verbose_name = "FAQ Sual"
        verbose_name_plural = "Tr FAQ Suallar"

    def __str__(self):
        return self.question
