from models.models import Articles
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import *

#create your view
@require_http_methods("GET")
def getAllArrticles(request):
        article = Articles.objects.all()
        data = {
                
                'Article':list(
                        article.values("id","title","summary",
                        "shortdesc","content","sid","status","author","pubdate"))
         }
        return JsonResponse(data)

            


