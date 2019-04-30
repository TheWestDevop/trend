from models.models import Articles
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import *

#create your view
@require_http_methods("GET")
def getAllArrticles(request):
        articles = Articles.objects.all()
        
        data = {}
        data['total']=Articles.objects.count()
        data['page']=1
        data['data']=[]
        items = []
        for article in articles:
           source   =  Articles.objects.raw("SELECT source,sourceurl FROM articles a,source b,subcategory c WHERE a.sid = b.id")
           item = {
              "title":article.title,
              "shortdescription":article.content[0:200],
              "author":article.author,
              "pubdate":article.pubdate,
              "content":article.content,
              "image":article.image,
              "source":source.source,
              "sourcelink":source.sourceurl
           }
           items.add(item) 
        data['data'] = items
        data['message'] = "successfully fetched articles"     

        return JsonResponse(data)

            
        

