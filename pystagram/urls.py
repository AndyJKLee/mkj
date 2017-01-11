from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings

from photo.views import photo_multiple, single_photo, new_photo

urlpatterns = [
    url(r'^$', photo_multiple, name='view_photos'),
    url(r'^photo/(?P<photo_id>\d+)/$', single_photo, name='view_single_photo'),
    url(r'^photo/upload/$', new_photo, name='new_photo'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', login, name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(r'^accounts/logout/', logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
