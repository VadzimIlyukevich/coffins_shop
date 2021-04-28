from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('coffin/', CoffinListView.as_view(), name='coffins_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('request/', RequestView.as_view(), name='request'),
    path('spa/', index),
]
