import os
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('apps.customer.public_urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls))),
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, "assets"))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def error_404(request, exception=None):
    return render(request, '404.html', status=404)


def error_500(request, exception=None):
    return render(request, '500.html', status=500)


def error_400(request, exception=None):
    return render(request, '400.html', status=400)


def error_403(request, exception=None):
    return render(request, '403.html', status=403)


handler500 = error_500
handler403 = error_403
handler400 = error_400
handler404 = error_404

