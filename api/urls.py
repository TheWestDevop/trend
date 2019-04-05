from django.conf.urls import url
from .views import list_article



urlpatterns = [
    url('', list_article ,name='list_article'),
]