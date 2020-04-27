"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


urlpatterns = [
    path('', include('apps.blog.urls')),
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

