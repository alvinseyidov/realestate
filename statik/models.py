from django.db import models


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

    def __str__(self):
        return f'Banner'


class Suallar(models.Model):
    text = models.CharField(max_length=256)
    link = models.CharField(max_length=256)

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


class FormSection(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256)
    text = models.TextField()
    form_button_text = models.CharField(max_length=256)
    form_button_link = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return f'Form bölməsi'


class MuzakireEdek(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    image = models.ImageField()

    def __str__(self):
        return 'SUALLARINIZ VAR? '



class Punktlar(models.Model):
    name = models.CharField(max_length=256)
    m = models.ForeignKey(MuzakireEdek, on_delete=models.CASCADE, related_name="punktlar")

    def __str__(self):
        return self.name


class MainSection(models.Model):
    title = models.TextField()
    text = models.TextField()
    text2 = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    background_image = models.ImageField()

    def __str__(self):
        return f'Main Section'




class WhySection(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return f'Why Section'

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

    def __str__(self):
        return f'Offers Section'


class FeedbackSection(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f'Feedback Section'