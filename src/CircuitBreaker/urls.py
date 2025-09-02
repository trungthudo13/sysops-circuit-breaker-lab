"""
URL configuration for CircuitBreaker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

import importlib

from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    re_path(
        "static/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.STATIC_ROOT,
            "show_indexes": False,
        },
    ),
    # Media files
    re_path(
        "media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
            "show_indexes": False,
        },
    ),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]


for app in settings.EXT_INSTALLED_APPS:
    try:
        importlib.import_module(f"{app}.urls")
    except ModuleNotFoundError:
        continue
    urlpatterns.append(path("", include(f"{app}.urls")))
