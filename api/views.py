from models.models import Articles
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import *


       
       summary = models.TextField()
       shortdesc = models.TextField()
       content = models.TextField()
       sid  = models.IntegerField()
       status = models.IntegerField()
       author = models.CharField(max_length=200)
       pubdate =  models.CharField(max_length=255)

#create your view
@require_GET()
def getAllArrticles(request):
        article =  Articles.objects.all()
        data = {
            'id':article.id,
            'title':article.title,
            'summary':article.summary,
            'shortdesc':article.shortdesc,
            'content':article.content,
            'sid':article.sid,
            'status':article.status,
            'author':article.author,
            'pubdate':article.pubdate
        }
        return JsonResponse(data)

            


