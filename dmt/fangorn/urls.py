from django.conf.urls.defaults import patterns, url
from dmt.fangorn.views import disk_tree_root, disk_tree_disks_nodes, generic_container_nodes

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'disk_tree_root/$', disk_tree_root),
    url(r'disk_tree_disks_nodes/$', disk_tree_disks_nodes),
    #url(r'disk/(?P<disk_id>\d+)/partition_nodes', partition_nodes),
    url(r'disk/(?P<disk_id>\d+)/partition_nodes', generic_container_nodes, {'model_name': 'Partition'}),
    url(r'disk/(?P<disk_id>\d+)/path_nodes', generic_container_nodes, {'model_name': 'Path'}),
)