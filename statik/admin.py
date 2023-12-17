from django.contrib import admin
from .models import *

admin.site.register(SortingSections)
admin.site.register(MainSection)
admin.site.register(WhySection)
admin.site.register(GeliriHesablaBanner)
admin.site.register(Suallar)
admin.site.register(SmartInvest)
admin.site.register(NiyeSecirler)
admin.site.register(FormSection)
admin.site.register(AdvantageSection)
admin.site.register(ProcessesSection)
admin.site.register(GetConsultationSection)
admin.site.register(OffersSection)
admin.site.register(FeedbackSection)




class PunkAdmin(admin.TabularInline):
    model = Punktlar

class MuzakireEdekAdmin(admin.ModelAdmin):
   inlines = [PunkAdmin,]

admin.site.register(MuzakireEdek,MuzakireEdekAdmin)


