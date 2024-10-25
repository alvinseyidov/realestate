from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core import views as core_views
from offer import views as offer_views
from calculator import views as calculator_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', core_views.index, name="index"),
    path('page/<str:link>/', core_views.page, name="page"),
    path('contactform/', core_views.contactform, name="contactform"),
    #path('contactformru/', core_views.contactformru, name="contactformru"),
    path('contactformtr/', core_views.contactformtr, name="contactformtr"),
    path('vebinarform/', core_views.vebinarform, name="vebinarform"),
    #path('vebinarformru/', core_views.vebinarformru, name="vebinarformru"),
    path('vebinarformtr/', core_views.vebinarformtr, name="vebinarformtr"),
    path('waitlist/', core_views.contactform2, name="waitlist"),
    path('offer/<int:id>/', offer_views.offer, name="offer"),
    path('offers/', offer_views.offers, name="offers"),
    path('tr/offer/<int:id>/', offer_views.offertr, name="offertr"),
    #path('ru/offer/<int:id>/', offer_views.offerru, name="offerru"),
    path('loadfaq/', offer_views.loadfaq, name="loadfaq"),
    path('tr/', core_views.tr, name="tr"),
    #path('ru/', core_views.ru, name="ru")
    path('data/<int:year>/<int:amount>/<int:mortgage>/', core_views.data, name="data"),
    path('test_data/', calculator_views.test, name="test"),
    path('calculate-investment/', calculator_views.calculate_investment_view, name='calculate-investment'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
