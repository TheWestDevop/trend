from rest_framework import serializers
from models.models import Articles


class ArticleSerializer(serializers.ModelSerializer):
      
        class Meta:
          model = Articles
          fields = ('id','title','summary','shortdesc',
          'content','sid','status','author','pubdate')
          read_only_fields = ('id','title','summary','shortdesc',
          'content','sid','status','author','pubdate')