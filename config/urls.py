from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('medias/', include('medias.urls', namespace='medias')),
    path('events/', include('events.urls', namespace='events')),
    path('team/', include('team.urls', namespace='team')),
    path('contacts/', include('contacts.urls', namespace='contacts'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)