from django.contrib import admin
from .models import *

admin.site.register(Message)
admin.site.register(Location)



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



class ImageTrAdmin(admin.TabularInline):
    model = ImageTR

class OfferTrAdmin(admin.ModelAdmin):
   inlines = [ImageTrAdmin,]

admin.site.register(OfferTR,OfferTrAdmin)