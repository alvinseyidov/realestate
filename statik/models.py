from django.db import models

class CoffeeSection(models.Model):
    title = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    user1_image = models.ImageField()
    user1_name = models.CharField(max_length=256)
    user1_profession = models.CharField(max_length=256)
    user2_image = models.ImageField()
    user2_name = models.CharField(max_length=256)
    user2_profession = models.CharField(max_length=256)



    class Meta:
        verbose_name = "Coffee Section"
        verbose_name_plural = "Coffee Section"
    def __str__(self):
        return f'Coffee Section'

class Form1(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    text1 = models.CharField(max_length=256)
    text2 = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Vebinara Yazıl"
        verbose_name_plural = "Form - Vebinara Yazıl"
    def __str__(self):
        return f'Vebinara yazıl formu'



class Form2(models.Model):
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Listing"
        verbose_name_plural = "Form - Listing"
    def __str__(self):
        return f'Form listing'



class Form3(models.Model):
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Özün tapmısan"
        verbose_name_plural = "Form - Özün tapmısan"
    def __str__(self):
        return f'Form Özün tapmısan'

class Form4(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Property Viewing"
        verbose_name_plural = "Form - Property Viewing"
    def __str__(self):
        return f'Form Property Viewing'

class Pages(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    body = models.TextField()

    class Meta:
        verbose_name = " Statik səhifələr"
        verbose_name_plural = " Statik səhifələr"
    def __str__(self):
        return self.title


class SortingSections(models.Model):
    main_section_active = models.BooleanField(default=True)
    main_section_sort = models.IntegerField()
    youtube_video_active = models.BooleanField(default=True)
    youtube_video_sort = models.IntegerField()
    why_active = models.BooleanField(default=True)
    why_sort = models.IntegerField()
    advantages_active = models.BooleanField(default=True)
    advantages_sort = models.IntegerField()
    processes_active = models.BooleanField(default=True)
    processes_sort = models.IntegerField()
    get_consultation_active = models.BooleanField(default=True)
    get_consultation_sort = models.IntegerField()
    faq_active = models.BooleanField(default=True)
    faq_sort = models.IntegerField()
    offers_active = models.BooleanField(default=True)
    offers_sort = models.IntegerField()
    feedbacks_active = models.BooleanField(default=True)
    feedbacks_sort = models.IntegerField()

    def __str__(self):
        return f'Bölmələrin sıralanması və idarəsi'


class GeliriHesablaBanner(models.Model):
    text = models.CharField(max_length=256)
    background_image = models.ImageField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Gəliri Hesablə Banneri"
        verbose_name_plural = "          Gəliri Hesablə Banneri"

    def __str__(self):
        return f'Banner'


class Suallar(models.Model):
    text = models.CharField(max_length=256)
    link = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Banner üzərindəki sual"
        verbose_name_plural = "         Banner üzərindəki suallar"
    def __str__(self):
        return self.text



class SmartInvest(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    image = models.ImageField()
    def __str__(self):
        return f'Niyə Smart Invest'

    class Meta:
        verbose_name = "Niyə Smart İnvest Bölməsi"
        verbose_name_plural = "        Niyə Smart İnvest Bölməsi"


class NiyeSecirler(models.Model):
    title = models.CharField(max_length=256)
    title1 = models.CharField(max_length=256)
    text1 = models.TextField()
    title2 = models.CharField(max_length=256)
    text2 = models.TextField()
    title3 = models.CharField(max_length=256)
    text3 = models.TextField()
    title4 = models.CharField(max_length=256)
    text4 = models.TextField()

    def __str__(self):
        return f'Ağıllı yatırımçılar niyə bizi seçirlər?'

    class Meta:
        verbose_name = "Niyə Bizi Seçirlər Punkt"
        verbose_name_plural = "      Niyə Bizi Seçirlər Punktlar"


class FormSection(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    text = models.TextField()
    form_button_text = models.CharField(max_length=256)
    form_button_link = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return f'Form bölməsi'

    class Meta:
        verbose_name = "Form Bölməsi"
        verbose_name_plural = "    Form Bölməsi"


class MuzakireEdek(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return 'SUALLARINIZ VAR? '

    class Meta:
        verbose_name = "Calendly Bölməsi"
        verbose_name_plural = "  Calendly Bölməsi"



class Punktlar(models.Model):
    name = models.CharField(max_length=256)
    m = models.ForeignKey(MuzakireEdek, on_delete=models.CASCADE, related_name="punktlar")

    def __str__(self):
        return self.name




class MainSection(models.Model):
    title = models.TextField()
    text = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    background_image = models.FileField()

    def __str__(self):
        return f'Main Section'

    class Meta:
        verbose_name = "Əsas Bölmə (1-ci bölmə)"
        verbose_name_plural = "             Əsas Bölmə (1-ci bölmə)"



class SliderSection(models.Model):
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return f'Slider Section'

    class Meta:
        verbose_name = "Slider Bölmə"
        verbose_name_plural = "            Slider Bölmə"


class WhySection(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return f'Why Section'

    class Meta:
        verbose_name = "Komanda Bölməsi"
        verbose_name_plural = " Komanda Bölməsi"

class AdvantageSection(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return f'Advantages Section'


class ProcessesSection(models.Model):
    title = models.CharField(max_length=256)
    process1_title = models.CharField(max_length=256)
    process1_text = models.CharField(max_length=256)
    process1_icon = models.FileField()
    process2_title = models.CharField(max_length=256)
    process2_text = models.CharField(max_length=256)
    process2_icon = models.FileField()
    process3_title = models.CharField(max_length=256)
    process3_text = models.CharField(max_length=256)
    process3_icon = models.FileField()
    process4_title = models.CharField(max_length=256)
    process4_text = models.CharField(max_length=256)
    process4_icon = models.FileField()


    def __str__(self):
        return f'Processes Section'

    class Meta:
        verbose_name = "Proseslər Bölməsi"
        verbose_name_plural = "           Proseslər Bölməsi"




class GetConsultationSection(models.Model):
    title = models.TextField()
    text = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)

    def __str__(self):
        return f'Get Consultation Section'

class OffersSection(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    form_text = models.CharField(max_length=256)
    form_button_text = models.CharField(max_length=256)
    form_button_url = models.CharField(max_length=256)

    title2 = models.CharField(verbose_name="Offer səhifəsində başlıq",max_length=256)
    title3 = models.CharField(verbose_name="Offer səhifəsində alt başlıq",max_length=256)

    def __str__(self):
        return f'Offers Section'

    class Meta:
        verbose_name = "Evlər, Villalar Bölməsi"
        verbose_name_plural = "     Evlər, Villalar Bölməsi"


class FeedbackSection(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f'Feedback Section'

    class Meta:
        verbose_name = "Müştəri Geribildirim Bölməsi"
        verbose_name_plural = "   Müştəri Geribildirim Bölməsi"



class CoffeeSectionRU(models.Model):
    title = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    user1_image = models.ImageField()
    user1_name = models.CharField(max_length=256)
    user1_profession = models.CharField(max_length=256)
    user2_image = models.ImageField()
    user2_name = models.CharField(max_length=256)
    user2_profession = models.CharField(max_length=256)



    class Meta:
        verbose_name = "Coffee Section"
        verbose_name_plural = "Ru Coffee Section"
    def __str__(self):
        return f'Coffee Section'

class Form1RU(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    text1 = models.CharField(max_length=256)
    text2 = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Vebinara Yazıl"
        verbose_name_plural = "Ru Form - Vebinara Yazıl"
    def __str__(self):
        return f'Vebinara yazıl formu'



class Form2RU(models.Model):
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Listing"
        verbose_name_plural = "Ru Form - Listing"
    def __str__(self):
        return f'Form listing'



class Form3RU(models.Model):
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Özün tapmısan"
        verbose_name_plural = "Ru Form - Özün tapmısan"
    def __str__(self):
        return f'Form Özün tapmısan'

class Form4RU(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Property Viewing"
        verbose_name_plural = "Ru Form - Property Viewing"
    def __str__(self):
        return f'Form Property Viewing'

class PagesRU(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    body = models.TextField()

    class Meta:
        verbose_name = " Statik səhifələr"
        verbose_name_plural = "Ru  Statik səhifələr"
    def __str__(self):
        return self.title


class SortingSectionsRU(models.Model):
    main_section_active = models.BooleanField(default=True)
    main_section_sort = models.IntegerField()
    youtube_video_active = models.BooleanField(default=True)
    youtube_video_sort = models.IntegerField()
    why_active = models.BooleanField(default=True)
    why_sort = models.IntegerField()
    advantages_active = models.BooleanField(default=True)
    advantages_sort = models.IntegerField()
    processes_active = models.BooleanField(default=True)
    processes_sort = models.IntegerField()
    get_consultation_active = models.BooleanField(default=True)
    get_consultation_sort = models.IntegerField()
    faq_active = models.BooleanField(default=True)
    faq_sort = models.IntegerField()
    offers_active = models.BooleanField(default=True)
    offers_sort = models.IntegerField()
    feedbacks_active = models.BooleanField(default=True)
    feedbacks_sort = models.IntegerField()

    def __str__(self):
        return f'Bölmələrin sıralanması və idarəsi'


class GeliriHesablaBannerRU(models.Model):
    text = models.CharField(max_length=256)
    background_image = models.ImageField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Gəliri Hesablə Banneri"
        verbose_name_plural = "Ru           Gəliri Hesablə Banneri"

    def __str__(self):
        return f'Banner'


class SuallarRU(models.Model):
    text = models.CharField(max_length=256)
    link = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Banner üzərindəki sual"
        verbose_name_plural = "Ru          Banner üzərindəki suallar"
    def __str__(self):
        return self.text



class SmartInvestRU(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    image = models.ImageField()
    def __str__(self):
        return f'Niyə Smart Invest'

    class Meta:
        verbose_name = "Niyə Smart İnvest Bölməsi"
        verbose_name_plural = "Ru         Niyə Smart İnvest Bölməsi"


class NiyeSecirlerRU(models.Model):
    title = models.CharField(max_length=256)
    title1 = models.CharField(max_length=256)
    text1 = models.TextField()
    title2 = models.CharField(max_length=256)
    text2 = models.TextField()
    title3 = models.CharField(max_length=256)
    text3 = models.TextField()
    title4 = models.CharField(max_length=256)
    text4 = models.TextField()

    def __str__(self):
        return f'Ağıllı yatırımçılar niyə bizi seçirlər?'

    class Meta:
        verbose_name = "Niyə Bizi Seçirlər Punkt"
        verbose_name_plural = "Ru       Niyə Bizi Seçirlər Punktlar"


class FormSectionRU(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    text = models.TextField()
    form_button_text = models.CharField(max_length=256)
    form_button_link = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return f'Form bölməsi'

    class Meta:
        verbose_name = "Form Bölməsi"
        verbose_name_plural = "Ru     Form Bölməsi"


class MuzakireEdekRU(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return 'SUALLARINIZ VAR? '

    class Meta:
        verbose_name = "Calendly Bölməsi"
        verbose_name_plural = "Ru   Calendly Bölməsi"



class PunktlarRU(models.Model):
    name = models.CharField(max_length=256)
    m = models.ForeignKey(MuzakireEdekRU, on_delete=models.CASCADE, related_name="punktlar")

    def __str__(self):
        return self.name




class MainSectionRU(models.Model):
    title = models.TextField()
    text = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    background_image = models.FileField()

    def __str__(self):
        return f'Main Section'

    class Meta:
        verbose_name = "Əsas Bölmə (1-ci bölmə)"
        verbose_name_plural = "Ru              Əsas Bölmə (1-ci bölmə)"



class SliderSectionRU(models.Model):
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return f'Slider Section'

    class Meta:
        verbose_name = "Slider Bölmə"
        verbose_name_plural = "Ru             Slider Bölmə"


class WhySectionRU(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return f'Why Section'

    class Meta:
        verbose_name = "Komanda Bölməsi"
        verbose_name_plural = "Ru  Komanda Bölməsi"

class AdvantageSectionRU(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return f'Advantages Section'


class ProcessesSectionRU(models.Model):
    title = models.CharField(max_length=256)
    process1_title = models.CharField(max_length=256)
    process1_text = models.CharField(max_length=256)
    process1_icon = models.FileField()
    process2_title = models.CharField(max_length=256)
    process2_text = models.CharField(max_length=256)
    process2_icon = models.FileField()
    process3_title = models.CharField(max_length=256)
    process3_text = models.CharField(max_length=256)
    process3_icon = models.FileField()
    process4_title = models.CharField(max_length=256)
    process4_text = models.CharField(max_length=256)
    process4_icon = models.FileField()


    def __str__(self):
        return f'Processes Section'

    class Meta:
        verbose_name = "Proseslər Bölməsi"
        verbose_name_plural = "Ru            Proseslər Bölməsi"




class GetConsultationSectionRU(models.Model):
    title = models.TextField()
    text = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)

    def __str__(self):
        return f'Get Consultation Section'

class OffersSectionRU(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    form_text = models.CharField(max_length=256)
    form_button_text = models.CharField(max_length=256)
    form_button_url = models.CharField(max_length=256)

    title2 = models.CharField(verbose_name="Offer səhifəsində başlıq",max_length=256)
    title3 = models.CharField(verbose_name="Offer səhifəsində alt başlıq",max_length=256)

    def __str__(self):
        return f'Offers Section'

    class Meta:
        verbose_name = "Evlər, Villalar Bölməsi"
        verbose_name_plural = "Ru      Evlər, Villalar Bölməsi"


class FeedbackSectionRU(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f'Feedback Section'

    class Meta:
        verbose_name = "Müştəri Geribildirim Bölməsi"
        verbose_name_plural = "Ru    Müştəri Geribildirim Bölməsi"






class CoffeeSectionTR(models.Model):
    title = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    user1_image = models.ImageField()
    user1_name = models.CharField(max_length=256)
    user1_profession = models.CharField(max_length=256)
    user2_image = models.ImageField()
    user2_name = models.CharField(max_length=256)
    user2_profession = models.CharField(max_length=256)



    class Meta:
        verbose_name = "Coffee Section"
        verbose_name_plural = "Tr Coffee Section"
    def __str__(self):
        return f'Coffee Section'

class Form1TR(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    text1 = models.CharField(max_length=256)
    text2 = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Vebinara Yazıl"
        verbose_name_plural = "Tr Form - Vebinara Yazıl"
    def __str__(self):
        return f'Vebinara yazıl formu'



class Form2TR(models.Model):
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Listing"
        verbose_name_plural = "Tr Form - Listing"
    def __str__(self):
        return f'Form listing'



class Form3TR(models.Model):
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Özün tapmısan"
        verbose_name_plural = "Tr Form - Özün tapmısan"
    def __str__(self):
        return f'Form Özün tapmısan'

class Form4TR(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    success_text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Form Property Viewing"
        verbose_name_plural = "Tr Form - Property Viewing"
    def __str__(self):
        return f'Form Property Viewing'

class PagesTR(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    body = models.TextField()

    class Meta:
        verbose_name = " Statik səhifələr"
        verbose_name_plural = "Tr  Statik səhifələr"
    def __str__(self):
        return self.title


class SortingSectionsTR(models.Model):
    main_section_active = models.BooleanField(default=True)
    main_section_sort = models.IntegerField()
    youtube_video_active = models.BooleanField(default=True)
    youtube_video_sort = models.IntegerField()
    why_active = models.BooleanField(default=True)
    why_sort = models.IntegerField()
    advantages_active = models.BooleanField(default=True)
    advantages_sort = models.IntegerField()
    processes_active = models.BooleanField(default=True)
    processes_sort = models.IntegerField()
    get_consultation_active = models.BooleanField(default=True)
    get_consultation_sort = models.IntegerField()
    faq_active = models.BooleanField(default=True)
    faq_sort = models.IntegerField()
    offers_active = models.BooleanField(default=True)
    offers_sort = models.IntegerField()
    feedbacks_active = models.BooleanField(default=True)
    feedbacks_sort = models.IntegerField()

    def __str__(self):
        return f'Bölmələrin sıralanması və idarəsi'


class GeliriHesablaBannerTR(models.Model):
    text = models.CharField(max_length=256)
    background_image = models.ImageField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Gəliri Hesablə Banneri"
        verbose_name_plural = "Tr           Gəliri Hesablə Banneri"

    def __str__(self):
        return f'Banner'


class SuallarTR(models.Model):
    text = models.CharField(max_length=256)
    link = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Banner üzərindəki sual"
        verbose_name_plural = "Tr          Banner üzərindəki suallar"
    def __str__(self):
        return self.text



class SmartInvestTR(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    image = models.ImageField()
    def __str__(self):
        return f'Niyə Smart Invest'

    class Meta:
        verbose_name = "Niyə Smart İnvest Bölməsi"
        verbose_name_plural = "Tr         Niyə Smart İnvest Bölməsi"


class NiyeSecirlerTR(models.Model):
    title = models.CharField(max_length=256)
    title1 = models.CharField(max_length=256)
    text1 = models.TextField()
    title2 = models.CharField(max_length=256)
    text2 = models.TextField()
    title3 = models.CharField(max_length=256)
    text3 = models.TextField()
    title4 = models.CharField(max_length=256)
    text4 = models.TextField()

    def __str__(self):
        return f'Ağıllı yatırımçılar niyə bizi seçirlər?'

    class Meta:
        verbose_name = "Niyə Bizi Seçirlər Punkt"
        verbose_name_plural = "Tr       Niyə Bizi Seçirlər Punktlar"


class FormSectionTR(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    text = models.TextField()
    form_button_text = models.CharField(max_length=256)
    form_button_link = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return f'Form bölməsi'

    class Meta:
        verbose_name = "Form Bölməsi"
        verbose_name_plural = "Tr     Form Bölməsi"


class MuzakireEdekTR(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return 'SUALLARINIZ VAR? '

    class Meta:
        verbose_name = "Calendly Bölməsi"
        verbose_name_plural = "Tr   Calendly Bölməsi"



class PunktlarTR(models.Model):
    name = models.CharField(max_length=256)
    m = models.ForeignKey(MuzakireEdekTR, on_delete=models.CASCADE, related_name="punktlar")

    def __str__(self):
        return self.name




class MainSectionTR(models.Model):
    title = models.TextField()
    text = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    background_image = models.FileField()

    def __str__(self):
        return f'Main Section'

    class Meta:
        verbose_name = "Əsas Bölmə (1-ci bölmə)"
        verbose_name_plural = "Tr              Əsas Bölmə (1-ci bölmə)"



class SliderSectionTR(models.Model):
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return f'Slider Section'

    class Meta:
        verbose_name = "Slider Bölmə"
        verbose_name_plural = "Tr             Slider Bölmə"


class WhySectionTR(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return f'Why Section'

    class Meta:
        verbose_name = "Komanda Bölməsi"
        verbose_name_plural = "Tr  Komanda Bölməsi"

class AdvantageSectionTR(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return f'Advantages Section'


class ProcessesSectionTR(models.Model):
    title = models.CharField(max_length=256)
    process1_title = models.CharField(max_length=256)
    process1_text = models.CharField(max_length=256)
    process1_icon = models.FileField()
    process2_title = models.CharField(max_length=256)
    process2_text = models.CharField(max_length=256)
    process2_icon = models.FileField()
    process3_title = models.CharField(max_length=256)
    process3_text = models.CharField(max_length=256)
    process3_icon = models.FileField()
    process4_title = models.CharField(max_length=256)
    process4_text = models.CharField(max_length=256)
    process4_icon = models.FileField()


    def __str__(self):
        return f'Processes Section'

    class Meta:
        verbose_name = "Proseslər Bölməsi"
        verbose_name_plural = "Tr            Proseslər Bölməsi"




class GetConsultationSectionTR(models.Model):
    title = models.TextField()
    text = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)

    def __str__(self):
        return f'Get Consultation Section'

class OffersSectionTR(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    form_text = models.CharField(max_length=256)
    form_button_text = models.CharField(max_length=256)
    form_button_url = models.CharField(max_length=256)

    title2 = models.CharField(verbose_name="Offer səhifəsində başlıq",max_length=256)
    title3 = models.CharField(verbose_name="Offer səhifəsində alt başlıq",max_length=256)

    def __str__(self):
        return f'Offers Section'

    class Meta:
        verbose_name = "Evlər, Villalar Bölməsi"
        verbose_name_plural = "Tr      Evlər, Villalar Bölməsi"


class FeedbackSectionTR(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f'Feedback Section'

    class Meta:
        verbose_name = "Müştəri Geribildirim Bölməsi"
        verbose_name_plural = "Tr    Müştəri Geribildirim Bölməsi"