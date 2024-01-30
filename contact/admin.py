from django.contrib import admin

from contact.models import Contact, Waitlist, Vebinar

admin.site.register(Contact)
admin.site.register(Vebinar)
admin.site.register(Waitlist)