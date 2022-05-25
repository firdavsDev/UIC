from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
]
