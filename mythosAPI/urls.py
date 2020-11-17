from mythosAPI.views import documentation
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('documentation', views.documentation, name='documentation'),
    # path('email', csrf_exempt(views.post), name="email"),

]