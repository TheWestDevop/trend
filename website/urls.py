from django.conf.urls import url
from manager.views import list_articles


urlpatterns = [
    url('', list_articles ,name='list_articles'),
]
