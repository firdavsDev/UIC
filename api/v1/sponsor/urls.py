
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('', SponsorViewSet, basename='sponsor')


urlpatterns = [
    
]

urlpatterns += router.urls
