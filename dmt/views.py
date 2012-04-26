from django.shortcuts import render_to_response
from django.template.context import RequestContext

from dmtcore.os import platinfo

def sysinfo(request):
    return render_to_response('sysinfo.html', {'sysinfo': platinfo.get_platform_details()},
                              context_instance = RequestContext(request))

