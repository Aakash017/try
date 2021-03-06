
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('trainee.urls')),
    path('users/', include('django.contrib.auth.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


