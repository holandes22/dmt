from django.conf.urls.defaults import patterns, url
from dmt.disks.views import DiskView, AllDisksDetailsView
from django.views.generic import ListView, DetailView
from dmt.disks.models import Disk, MultipathDisk

urlpatterns = patterns('dmt.disks.views',
        url(r'force_refresh_disk_objects$', 'force_refresh_disk_objects', name='force_refresh_disk_objects'),
        url(r'show_all_disks$', 'show_all_disks', name='show_all_disks'),
        url(r'disk_list$', DiskView.as_view(), name='disk_list'),
        url(r'disk_list2$', ListView.as_view(model=Disk, context_object_name='disks'), name='disk_list2'),
        url(r'(?P<disk_id>\d+)/partitions', 'show_disk_partitions', name='show_disk_partitions'),
        #####
        url(r'all/details$', AllDisksDetailsView.as_view(), name='all_disks_details'),
        url(r'basic/list$', ListView.as_view(model=Disk, context_object_name='disks'), name='basic_disks_list'),
        url(r'multipath/list$', ListView.as_view(
                                                 model=MultipathDisk,
                                                 template_name='disks/disk_list.html',
                                                 context_object_name='disks'
                                                 ), name='multipath_disks_list'),
        url(r'basic/(?P<pk>\d+)/details', DetailView.as_view(model=Disk), name='basic_disk_details'),
        url(r'multipath/(?P<pk>\d+)/details', DetailView.as_view(
                                                                 model=MultipathDisk,
                                                                 template_name='disks/disk_detail.html',
                                                                 ), name='multipath_disk_details'),
        
        )
