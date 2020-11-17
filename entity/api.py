from rest_framework import permissions, viewsets
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from entity.models import Entity
from .serializers import EntitySerializer


class EntityViewSet(viewsets.ModelViewSet):
    fields = ('name', 'origin', 'parents')

    def list(self, request):
        queryset = Entity.objects.all()

        serializer = EntitySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, name=None):
        queryset = Entity.objects.all()
        if name.isdigit():
            entity = get_object_or_404(queryset, pk=name)
        else:
            entity = get_object_or_404(queryset, name=name)

        serializer = EntitySerializer(entity)
        return Response(serializer.data)

    def filter(self, request, pk=None, *args, **kwargs):
        print(kwargs)
        queryset = Entity.objects.raw(
            "select * FROM entity_entity WHERE origin = '%s'" % kwargs.get('origin'))
        serializer = EntitySerializer(queryset, many=True)
        return Response(serializer.data)




