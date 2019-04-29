from models.models import Articles
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import *

#create your view
@require_http_methods("GET")
def getAllArrticles(request):
        MAX_OBJECTS = 20
        pageNum = request.GET.get('page',1)
        article = Articles.objects.all()[:MAX_OBJECTS]
        paginator = Paginator(article,10)
        pages = paginator.page(pageNum)
        data = {
                
                'Article':list(pages,
                        article.values("id","title","summary",
                        "shortdesc","content","sid","status","author","pubdate"))
         }
        return JsonResponse(data)

            


