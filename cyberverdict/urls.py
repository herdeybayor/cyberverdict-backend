from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

admin.site.site_header = "Cyberverdict Admin"
admin.site.index_title = "Admin"
admin.site.site_title = "Cyberverdict Admin"

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="schema-docs",
    ),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + debug_toolbar_urls()
    )
