from django.urls import path
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('coffin', CoffinApiViewsSet, basename='coffin')
router.register('requests', RequestApiViewsSet, basename='requests')
router.register('form', FormOfCoffinDetailApiViewsSet, basename='form')
urlpatterns = []
urlpatterns += router.urls
