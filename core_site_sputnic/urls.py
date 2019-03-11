from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core_site_sputnic import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sputnic.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

