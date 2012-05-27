from django.conf.urls.defaults import patterns, url
from dmt.fangorn.views import DiskRootNodeJSONView, DiskNodesJSONView, PartitionNodesJSONView, PathNodesJSONView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'disk/root/$', DiskRootNodeJSONView.as_view(), name='tree_disk_root'),
    url(r'disk/disk_nodes/$', DiskNodesJSONView.as_view(), name='disk_root_children_nodes'),
    url(r'disk/(?P<disk_id>\d+)/partition_nodes/$', PartitionNodesJSONView.as_view()),
    url(r'disk/(?P<disk_id>\d+)/path_nodes/$', PathNodesJSONView.as_view()),
)
