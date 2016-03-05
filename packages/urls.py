from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^versions/(?P<package_id>[0-9]+)$', views.versions, name='versions'),
    url(r'^details/(?P<package_version_id>[0-9]+)$', views.details, name='details'),
    url(r'^download_package/(?P<package_version_id>[0-9]+)$', views.download_package, name='download_package'),
    url(r'^download_manual/(?P<package_version_id>[0-9]+)$', views.download_manual, name='download_manual'),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^api/1.0/packages/$', views.PackageView.as_view(), name='package-list'),
    url(r'^api/1.0/packageversions/$', views.PackageVersionView.as_view(), name='package-version-list'),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^customers/([0-9]+)/$', views.CustomerProductList.as_view()),
]
