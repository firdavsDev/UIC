from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
# Create your views here.

class SponsorViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'list', 'retrieve']:
            # which is permissions.IsAdminUser 
            self.permission_classes = [IsAdminUser]
        else :
            self.permission_classes = [AllowAny]
            # which is permissions.AllowAny - create
        return super(SponsorViewSet, self).get_permissions()
    