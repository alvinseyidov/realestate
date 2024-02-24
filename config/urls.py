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
    path('page/<str:link>/', core_views.page, name="page"),
    path('contactform/', core_views.contactform, name="contactform"),
    path('vebinarform/', core_views.vebinarform, name="vebinarform"),
    path('data/<int:year>/<int:amount>/<int:mortgage>/', core_views.data, name="data"),
    path('waitlist/', core_views.contactform2, name="waitlist"),
    path('offer/<int:id>/', offer_views.offer, name="offer"),
    path('loadfaq/', offer_views.loadfaq, name="loadfaq"),
    path('tr/', core_views.tr, name="tr"),
    path('ru/', core_views.ru, name="ru")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
