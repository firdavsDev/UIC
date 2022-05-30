from django.contrib import admin
from django.conf import settings
from django.http import Http404, HttpResponseServerError
from .views import RegisterApi
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)
#Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title='UIC Group API',
        description="UIC Group's API",
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email="xackercoder@gmail.com@gmail.com"),
        license=openapi.License(name='MetSenat License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)



urlpatterns = [
    # url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('api/sponsor/', include('api.v1.sponsor.urls')),
    path('api/student/', include('api.v1.student.urls')),
    path('api/token/register/', RegisterApi.as_view(), name='api_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #Swagger UI documentation
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Error handlers
handler404 = lambda request, exception: Http404('Not found')
handler500 = lambda request: HttpResponseServerError("Internal Server Error")
