from django.conf.urls.defaults import patterns, url
from dmt.disks.views import force_refresh_disk_objects, show_all_disks, show_disk_partitions

urlpatterns = patterns('',
        url(r'disks/force_refresh_disk_objects$', force_refresh_disk_objects),
        url(r'disks/show_all_disks$', show_all_disks),
        url(r'disks/(?P<disk_id>\d+)/partitions', show_disk_partitions),
        )
