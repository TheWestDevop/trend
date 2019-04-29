from django.conf.urls import url,include
from .views import *




urlpatterns = [
    url('',include(router.urls)),
]