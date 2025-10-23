from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.views import HealthCheckView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # path('', IndexView.as_view(), name='index'),
    path('health/', HealthCheckView.as_view(), name='health_check'),
]

# handler404 = Custom404View.as_view()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), *urlpatterns]
