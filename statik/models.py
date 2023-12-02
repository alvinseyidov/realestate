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


class MainSection(models.Model):
    title = models.TextField()
    text = models.TextField()
    text2 = models.TextField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    background_image = models.ImageField()

    def __str__(self):
        return f'Main Section'


class VideoSection(models.Model):
    title = models.TextField()
    text = models.TextField()
    background_image = models.ImageField()
    video_image = models.ImageField()
    video_file = models.FileField()

    def __str__(self):
        return f'Video Section'


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
    process1 = models.CharField(max_length=256)
    process1_icon = models.FileField()
    process2 = models.CharField(max_length=256)
    process2_icon = models.FileField()
    process3 = models.CharField(max_length=256)
    process3_icon = models.FileField()
    process4 = models.CharField(max_length=256)
    process4_icon = models.FileField()
    process5 = models.CharField(max_length=256)
    process5_icon = models.FileField()
    button_text = models.CharField(max_length=256)
    button_link = models.CharField(max_length=256)
    background_image = models.ImageField()

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