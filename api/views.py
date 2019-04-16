from models.models import Articles
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins,viewsets
from .serializer import ArticleSerializer


class  StandardResultsetPagination(PageNumberPagination):
       page_size = 10
       page_size_query_param = 'page_size'
       max_page_size = 1000
       

#create your view
class ArticleView(viewsets.ModelViewSet):
        pagination_class = StandardResultsetPagination
        queryset = Articles.objects.all() 
        paginate_by = 10
        serializer_class =  ArticleSerializer  
        serializer = serializer_class(queryset,many=True)    


