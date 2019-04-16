from django.conf.urls import url,include
from .views import ArticleView
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)

router.register('',ArticleView,base_name='Articles')

urlpatterns = [
    url('',include(router.urls)),
]