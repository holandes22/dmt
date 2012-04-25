from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin

from dmt.settings import STATIC_ROOT, DEBUG


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='main.html')),
    url(r'^disks/', include('dmt.disks.urls')),
    url(r'^tree/', include('dmt.fangorn.urls')),

)

if DEBUG:
    urlpatterns += patterns(url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),)
