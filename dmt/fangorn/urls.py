from django.conf.urls.defaults import patterns, url
from dmt.fangorn.views import DiskRootNodeJSONView, DiskNodesJSONView, GenericNodeContainerJSONView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'disk/root/$', DiskRootNodeJSONView.as_view()),
    url(r'disk/disk_nodes/$', DiskNodesJSONView.as_view()),
    url(r'disk/(?P<disk_id>\d+)/partition_nodes/$', GenericNodeContainerJSONView.as_view(), {'model_name': 'Partition'}),
    url(r'disk/(?P<disk_id>\d+)/path_nodes/$', GenericNodeContainerJSONView.as_view(), {'model_name': 'Path'}),
)