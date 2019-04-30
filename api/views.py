from models.models import Articles,Source
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import *

#create your view
@require_http_methods("GET")
def getAllArrticles(request):
        articles = Articles.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(articles)
        try:
           pages = paginator.page(page)
        except PageNotAnInteger:
               pages = paginator.page(1) 
        except EmptyPage:
                pages = paginator.page(paginator.num_pages)       
        data = {}
        data['total']=Articles.objects.count()
        data['page']=pages
        data['data']=[]
        items = []
        for article in articles:
          for sources   in  Source.objects.raw("SELECT b.id,b.name,b.url FROM models_source b,models_articles a WHERE b.id = %s ",[article.sid]):
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
           items.append(item) 
        data['data'] = items
        data['message'] = "successfully fetched articles"     

        return JsonResponse(data)

            
        

