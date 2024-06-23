from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filters-and-tables', views.filters_page, name='filters_page'),
    path('contact', views.contact_us, name='contact_us'),
    path('compare', views.compare_page, name='compare_page'),
    path('hc-data', views.old_hc_data_page, name='old_hc_data_page'),
]