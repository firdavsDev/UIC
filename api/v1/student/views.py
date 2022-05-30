from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = StudentSerializer
    
    