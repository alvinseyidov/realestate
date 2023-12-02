from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core import views as core_views
from offer import views as offer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', core_views.index, name="index"),
    path('contactform/', core_views.contactform, name="contactform"),
    path('waitlist/', core_views.contactform2, name="waitlist"),
    path('offer/<int:id>/', offer_views.offer, name="offer")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
