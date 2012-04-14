from django.conf.urls.defaults import patterns, url
from dmt.disk.views import force_refresh_disk_objects, show_all_disks, show_disk_partitions

urlpatterns = patterns('',
        url(r'disk/force_refresh_disk_objects$', force_refresh_disk_objects),
        url(r'disk/show_all_disks$', show_all_disks),
        url(r'disk/(?P<disk_id>\d+)/partitions', show_disk_partitions),
        )
