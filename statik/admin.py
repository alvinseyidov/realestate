from django.contrib import admin
from .models import *

from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class PagesAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Pages, PagesAdmin)

admin.site.register(Form1)
admin.site.register(Form2)
admin.site.register(Form3)
admin.site.register(Form4)
admin.site.register(CoffeeSection)

admin.site.register(MainSection)
admin.site.register(SliderSection)
admin.site.register(WhySection)
admin.site.register(GeliriHesablaBanner)
admin.site.register(Suallar)
admin.site.register(SmartInvest)
admin.site.register(NiyeSecirler)
admin.site.register(FormSection)
admin.site.register(ProcessesSection)
admin.site.register(OffersSection)
admin.site.register(FeedbackSection)


admin.site.register(Form1RU)
admin.site.register(Form2RU)
admin.site.register(Form3RU)
admin.site.register(Form4RU)
admin.site.register(CoffeeSectionRU)

admin.site.register(MainSectionRU)
admin.site.register(SliderSectionRU)
admin.site.register(WhySectionRU)
admin.site.register(GeliriHesablaBannerRU)
admin.site.register(SuallarRU)
admin.site.register(SmartInvestRU)
admin.site.register(NiyeSecirlerRU)
admin.site.register(FormSectionRU)
admin.site.register(ProcessesSectionRU)
admin.site.register(OffersSectionRU)
admin.site.register(FeedbackSectionRU)




class PunkAdmin(admin.TabularInline):
    model = Punktlar

class MuzakireEdekAdmin(admin.ModelAdmin):
   inlines = [PunkAdmin,]

admin.site.register(MuzakireEdek,MuzakireEdekAdmin)


