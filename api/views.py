from models.models import Articles,Source
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
           sources   =  Source.objects.raw("SELECT name,url FROM source b,articles a WHERE b.id = %s",[article.sid])
           item = {
              "title":article.title,
              "shortdescription":article.content[0:200],
              "author":article.author,
              "pubdate":article.pubdate,
              "content":article.content,
              "image":article.imageurl,
              "source":sources.name,
              "sourcelink":sources.url
           }
           items.add(item) 
        data['data'] = items
        data['message'] = "successfully fetched articles"     

        return JsonResponse(data)

            
        

