from django.conf import settings
from django.conf.urls import handler500
from django.urls import re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

handler500  # Pyflakes

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view()),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
