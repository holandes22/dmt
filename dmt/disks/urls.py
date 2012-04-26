from django.conf.urls.defaults import patterns, url
from dmt.disks.views import AllDisksDetailsView
from django.views.generic import ListView, DetailView
from dmt.disks.models import Disk, MultipathDisk, Partition, Path

urlpatterns = patterns('dmt.disks.views',
        url(r'force_refresh_disk_objects$', 'force_refresh_disk_objects', name='force_refresh_disk_objects'),
        url(r'all/details$', AllDisksDetailsView.as_view(), name='all_disks_details'),
        url(r'basic/list$', ListView.as_view(model=Disk,
                                             template_name='disks/generic_list.html'), name='basic_disk_list'),
        url(r'multipath/list$', ListView.as_view(
                                                 model=MultipathDisk,
                                                 template_name='disks/generic_list.html', ), 
            name='multipath_disk_list'),
        url(r'basic/(?P<pk>\d+)/details', DetailView.as_view(
                                                             model=Disk,
                                                             template_name='disks/generic_detail.html',
                                                             ), name='basic_disk_detail'),
        url(r'multipath/(?P<pk>\d+)/details', DetailView.as_view(
                                                                 model=MultipathDisk,
                                                                 template_name='disks/generic_detail.html',
                                                                 ), name='multipath_disk_detail'),
        url(r'basic/(?P<pk>\d+)/partition/list', ListView.as_view(
                                                                  model=Partition,
                                                                  template_name='disks/generic_list.html',
                                                                  ), name='partition_list'),
        url(r'partition/(?P<pk>\d+)/details', 
            DetailView.as_view(
                                model=Partition,
                                template_name='disks/generic_detail.html',
                                ),name='partition_detail'),
        url(r'multipath/(?P<pk>\d+)/path/list', ListView.as_view(
                                                                  model=Path,
                                                                  template_name='disks/generic_list.html',
                                                                  ), name='path_list'),
        url(r'path/(?P<pk>\d+)/details', 
            DetailView.as_view(
                                model=Path,
                                template_name='disks/generic_detail.html',
                                ),name='path_detail'),
        )
