from django.contrib import admin
from .models import *

admin.site.register(Message)



class ImageAdmin(admin.TabularInline):
    model = Image

class OfferAdmin(admin.ModelAdmin):
   inlines = [ImageAdmin,]

admin.site.register(Offer,OfferAdmin)


class ImageRuAdmin(admin.TabularInline):
    model = ImageRU

class OfferRuAdmin(admin.ModelAdmin):
   inlines = [ImageRuAdmin,]

admin.site.register(OfferRU,OfferRuAdmin)