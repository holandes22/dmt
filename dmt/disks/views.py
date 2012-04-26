from django.db.models import permalink
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, DetailView

from dmt.disks.tasks import refresh_disk_models
from dmt.disks.models import Disk, Partition, MultipathDisk

def force_refresh_disk_objects(request):
    response = refresh_disk_models.delay()
    response.get()
    return show_all_disks(request)

def show_all_disks(request):
    disks = Disk.objects.all()
    return render_to_response('disks.html', {'disks': disks},
            context_instance=RequestContext(request))

def show_disk_partitions(request, disk_id):
    partitions = Partition.objects.filter(parent = disk_id)
    return render_to_response('partitions.html', {'partitions': partitions},
            context_instance = RequestContext(request))

class DiskView(TemplateView):

    template_name = 'disks/disk_list.html'

    def get_context_data(self, **kwargs):
        context = super(DiskView, self).get_context_data(**kwargs)
        context['disks'] = Disk.objects.all()
        return context
    
class AllDisksDetailsView(TemplateView):
    template_name = 'disks/all_disks_details.html'
    
    def get_context_data(self, **kwargs):
        context = super(AllDisksDetailsView, self).get_context_data(**kwargs)
        context['basic_disks'] = Disk.objects.all()
        context['mp_disks'] = MultipathDisk.objects.all()
        return context
    
    @classmethod
    @permalink
    def get_permalink(cls):
        return ('all_disks_details', [])  
