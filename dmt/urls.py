from dmt.settings import STATIC_ROOT, DEBUG
from django.conf.urls import patterns, include, url
from dmt.celerytest.views import list_disks_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'storagemon.views.home', name='home'),
    # url(r'^storagemon/', include('storagemon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^list_disks/', list_disks_view),
)

if DEBUG:
    urlpatterns += patterns(url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),)
