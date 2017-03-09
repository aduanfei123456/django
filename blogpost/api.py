from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission
from rest_framework import serializers,viewsets
from rest_framework.response import Response
from blogpost.models import Blogpost
from rest_framework import permissions
class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Blogpost
        fields=('title','author','body','slug')
#A ViewSet class is simply a type of class-based View, that does not provide any method handlers
# such as .get() or .post(), and instead provides actions such as .list() and .create().
class BlogpostSet(viewsets.ModelViewSet):

    queryset=Blogpost.objects.all()
    serializer_class=BlogpostSerializer
    def list(self,request):
        search_param=self.request.query_params.get('title',None)
        if search_param is not None:
            queryset=Blogpost.objects.filter(title__contains=search_param)
        serializer=BlogpostSerializer(queryset,many=True)
        return Response(serializer.data)



