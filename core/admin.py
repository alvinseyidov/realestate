from django.contrib import admin
from .models import *

admin.site.register(General)
admin.site.register(Social)
admin.site.register(Feature)
admin.site.register(Why)
admin.site.register(FAQ)
admin.site.register(Feedback)
admin.site.register(FeedbackTR)
admin.site.register(Parametr)
admin.site.register(CalendlyScript)
admin.site.register(Slider)
admin.site.register(SliderTR)


admin.site.register(GeneralRU)
admin.site.register(FeatureRU)
admin.site.register(WhyRU)
admin.site.register(FAQRU)
admin.site.register(FeedbackRU)
admin.site.register(SliderRU)

class BodyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
admin.site.register(Body,BodyAdmin)

