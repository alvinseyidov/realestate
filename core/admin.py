from django.contrib import admin
from .models import *

admin.site.register(General)
admin.site.register(Social)
admin.site.register(Feature)
admin.site.register(Why)
admin.site.register(FAQ)
admin.site.register(Feedback)
admin.site.register(Parametr)
admin.site.register(Slider)

class BodyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
admin.site.register(Body,BodyAdmin)

