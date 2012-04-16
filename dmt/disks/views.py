
from dmt.disks.tasks import refresh_disk_models
from dmt.disks.models import Disk, Partition

from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

def force_refresh_disk_objects(request):
    response = refresh_disk_models.delay()
    response.get()
    return show_all_disks(request)

def show_all_disks(request):
    disks = Disk.objects.all()
    return render_to_response('disks.html', {'disks': disks},
            context_instance = RequestContext(request))

def show_disk_partitions(request, disk_id):
    partitions = Partition.objects.filter(parent = disk_id)
    return render_to_response('partitions.html', {'partitions': partitions},
            context_instance = RequestContext(request))


class DiskView(TemplateView):

    template_name = 'disk/disks
