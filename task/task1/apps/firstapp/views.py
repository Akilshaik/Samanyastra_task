from django.shortcuts import render
from django.http import JsonResponse
from apps.firstapp.models import Person


# Create your views here.

def home(request):
    return render(request, 'index.html')

def health(request):
    data={
        'status': True
    }
    return JsonResponse(data, status=200)

def persons(request):
    personData= Person.objects.all().values()
    pdata=list(personData)
    return JsonResponse(pdata, safe=False )
    