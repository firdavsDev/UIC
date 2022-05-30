
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('', StudentViewSet, basename='student')


urlpatterns = [
    
]

urlpatterns += router.urls
