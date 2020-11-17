from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Entity
# Create your views here.
def index(request):

	return render(request, 'entities/entity.html')

def list(request):
	entity = Entity.objects.all()

	context = {
		'entities': entity
	}
	return render(request, 'entities/entities.html', context)

def single(request, entityID):
	entity = get_object_or_404(Entity, pk=entityID)

	context = {
		'entity': entity
	}

	return render(request, 'entities/entity.html', context)