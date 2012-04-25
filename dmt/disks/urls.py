from django.conf.urls.defaults import patterns, url
from dmt.disks.views import DiskView, AllDisksDetailsView
from django.views.generic import ListView
from dmt.disks.models import Disk

urlpatterns = patterns('dmt.disks.views',
        url(r'force_refresh_disk_objects$', 'force_refresh_disk_objects', name='force_refresh_disk_objects'),
        url(r'show_all_disks$', 'show_all_disks', name='show_all_disks'),
        url(r'disk_list$', DiskView.as_view(), name='disk_list'),
        url(r'disk_list2$', ListView.as_view(model=Disk, context_object_name='disks'), name='disk_list2'),
        url(r'(?P<disk_id>\d+)/partitions', 'show_disk_partitions', name='show_disk_partitions'),
        #####
        url(r'all/details$', AllDisksDetailsView.as_view(), name='all_disks_details'),
        )
