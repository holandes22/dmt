from django.template.context import RequestContext
from django.shortcuts import render_to_response
from dmt.celerytest.tasks import  list_disks_task


def list_disks_view(request):
    result = list_disks_task.delay()
    return render_to_response('disks.html', {'disks': result.get()},
                                          context_instance = RequestContext(request))
