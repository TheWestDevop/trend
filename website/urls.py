from django.urls import path
from manager.views import list_articles,create_article,delete_article,update_article

urlpatterns = [
    path('',list_articles,name="list_articles"),
    path('new',create_article,name="create_article"),
    path('update/<int:id>/',update_article,name="update_article"),
    path('delete/<int:id>/',delete_article,name="delete_article"),
]

    