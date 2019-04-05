from django.shortcuts import render
from models.models import Articles
from django.http import JsonResponse


def list_article(request):
    template_name = 'articles.html'
    article = Articles.objects.all().values()
    article_list = list(article)
    return JsonResponse(article_list,safe=False)