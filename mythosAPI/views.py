from django.shortcuts import render
from django.template import RequestContext
from .forms import emailForm
from django.core.mail import send_mail
from entity.models import Entity


# Create your views here.
##url request 
def index(request): 
  if request.method == 'POST':
    form = emailForm(request.POST)
    if form.is_valid():
      subject = form.cleaned_data['subject']  
      message = form.cleaned_data['message']  
      send_mail(subject, message, 'mythosAPI@gmail.com', ['parmjit.singh.1199@gmail.com'], fail_silently=False)
    else:
      form = emailForm()

  
  return render(request, 'mythosAPI_Pages/index.html', {'form': emailForm()})
  # data = [{'Name': 'Prometheus', 'Description': 'Titan', 'Origin': 'Greek','Role': 'Hero', 'Traits': 'Regeneration', 'Greatest Feats': 'Giving fire to humans', 'Image': 'path/to/image.jpg'}]
  # return JsonResponse(data, safe=False)
  # return HttpResponse('<h1>First Response in Django</h1>')

def about(request):
  return render(request, 'mythosAPI_Pages/about.html')

def documentation(request):
  return render(request, 'mythosAPI_Pages/documentation.html')

def post(request):
  form = request.POST.get("subject")
  print(form)
  return render(request, 'mythosAPI_Pages/index.html')
