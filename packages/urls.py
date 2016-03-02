from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^versions/(?P<package_id>[0-9]+)$', views.versions, name='versions'),
    url(r'^details/(?P<package_version_id>[0-9]+)$', views.details, name='details'),
    url(r'^download_package/(?P<package_version_id>[0-9]+)$', views.download_package, name='download_package'),
    url(r'^download_manual/(?P<package_version_id>[0-9]+)$', views.download_manual, name='download_manual'),
]
