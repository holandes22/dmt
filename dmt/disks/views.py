from django.db.models import permalink
from django.views.generic import TemplateView
from django.http import HttpResponse

from dmt.disks.tasks import refresh_disk_models
from dmt.disks.models import Disk, MultipathDisk


def force_refresh_disk_objects(request):
    response = refresh_disk_models.delay()
    response.get()
    return HttpResponse("<html>Done</html>")


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
