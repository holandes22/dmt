from itertools import chain

from django import http
from django.db.models import get_model
from django.utils import simplejson as json
from django.views.generic.base import View

from dmt.fangorn.node import DynatreeNode
from dmt.disks.models import Disk, MultipathDisk, Partition, Path
from dmt.disks.views import AllDisksDetailsView


class JSONResponseMixin(object):
    
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return json.dumps(context)
    
    def _get_filter_queryset(self, app_name, model_name, **kwargs):
        model = get_model(app_name, model_name)
        return model.objects.filter(**kwargs)
        
    
class DiskRootNodeJSONView(JSONResponseMixin, View):
    
    def get(self, request, *args, **kwargs):
        node = DynatreeNode()
        node.node_attrs["title"] = "Disks"
        node.node_attrs["isFolder"] = True
        node.node_attrs["key"] = "disks_root_node"
        node.node_attrs["url"] = AllDisksDetailsView.get_permalink()
        node.node_attrs["isLazy"] = True
        node.node_attrs["lazyLoadingUrl"] = "/tree/disk/disk_nodes/"    
        return self.render_to_response(node.node_attrs)
    
   
class DiskNodesJSONView(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        children = []
        disks = list(chain(Disk.objects.all(), MultipathDisk.objects.all()))
        for disk in disks:
            node = DynatreeNode()
            node.node_attrs['title'] = disk.get_node_title()
            node.node_attrs['url'] = "/todo"
            node.node_attrs['isFolder'] = True
            
            node_child = DynatreeNode()
            node_child.node_attrs['title'] = disk.name
            node_child.node_attrs['url'] = "/todo"
            node_child.node_attrs['isFolder'] = True
            node_child.node_attrs['isLazy'] = True,
            node_child.node_attrs['lazyLoadingUrl'] = disk.get_children_lazy_loading_url()
            node.node_attrs['children'] = [node_child.node_attrs]
            children.append(node.node_attrs)
        return self.render_to_response(children)
    
 
class DiskChildrenNodesBaseView(JSONResponseMixin, View):
    
    model = None
    
    def get(self, request, disk_id, *args, **kwargs):
        children = []
        #if not request.user.is_anonymous():
        node = DynatreeNode()
        node.node_attrs['title'] = self.model._meta.verbose_name_plural.title()
        node.node_attrs['url'] = "/todo"
        node.node_attrs['isFolder'] = True
        node.node_attrs['isLazy'] = False,
        node.node_attrs['children'] = []
        objects = self.model.objects.filter(parent=disk_id)
        for obj in objects:
            node_child = DynatreeNode()
            node_child.node_attrs['title'] = obj.name
            node_child.node_attrs['url'] = "/todo/get_from_model_url"
            node_child.node_attrs['isFolder'] = False
            node.node_attrs['children'].append(node_child.node_attrs)
        children.append(node.node_attrs)
        return self.render_to_response(children)
    
class PartitionNodesJSONView(DiskChildrenNodesBaseView):
    model = Partition
    
class PathNodesJSONView(DiskChildrenNodesBaseView):
    model = Path   
    
