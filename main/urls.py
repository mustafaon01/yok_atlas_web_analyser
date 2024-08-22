from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filters-and-tables', views.filters_page, name='filters_page'),
    path('contact', views.contact_us, name='contact_us'),
    path('hc-data', views.old_hc_data_page, name='old_hc_data_page'),
    path('high-school', views.high_school_page, name='high_school_page'),
    path('preference_tendency', views.preference_tendency_view, name='preference_tendency_view'),
    path('tercih_sihirbazi', views.tercih_sihirbazi, name='tercih_sihirbazi'),
]
