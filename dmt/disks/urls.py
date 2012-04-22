from django.conf.urls.defaults import patterns, url
from dmt.disks.views import force_refresh_disk_objects, show_all_disks, show_disk_partitions
from dmt.disks.views import DiskView
from django.views.generic import ListView
from dmt.disks.models import Disk

urlpatterns = patterns('',
        url(r'disks/force_refresh_disk_objects$', force_refresh_disk_objects, name='force_refresh_disk_objects'),
        url(r'disks/show_all_disks$', show_all_disks),
        url(r'disks/disk_list$', DiskView.as_view()),
        url(r'disks/disk_list2$', ListView.as_view(model=Disk, context_object_name='disks'), name='disk_list2'),
        url(r'disks/(?P<disk_id>\d+)/partitions', show_disk_partitions),
        )
