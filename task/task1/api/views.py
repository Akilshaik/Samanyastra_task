from django.shortcuts import render
from rest_framework import viewsets, generics
from api.models import pepoles
from api.serializers import pepolesSerializers

# Create your views here.
def homepage(request):
    return render(request, 'rest.html')


class pepolesViewSet(viewsets.ModelViewSet):
    queryset= pepoles.objects.all()
    serializer_class= pepolesSerializers




class pepoleList(generics.ListAPIView):
    queryset=pepoles.objects.all()
    serializer_class=pepolesSerializers

class pepoleDetail(generics.RetrieveAPIView):
    queryset=pepoles.objects.all()
    serializer_class=pepolesSerializers

class pepolesCreateView(generics.CreateAPIView):
    queryset = pepoles.objects.all()
    serializer_class = pepolesSerializers

class pepolesUpdateView(generics.UpdateAPIView):
    queryset = pepoles.objects.all()
    serializer_class = pepolesSerializers

class pepolesDeleteView(generics.DestroyAPIView):
    queryset = pepoles.objects.all()  