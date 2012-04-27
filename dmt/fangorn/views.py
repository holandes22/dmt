import os

from django import http
from django.db.models import get_model, permalink
from django.utils import simplejson as json
from django.views.generic.base import View

from dmt.settings import STATIC_URL
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
        node.node_attrs["imagePath"] = os.path.join(STATIC_URL, 'img', 'fangorn')
        node.node_attrs["isFolder"] = True
        node.node_attrs["key"] = "disks_root_node"
        node.node_attrs["url"] = AllDisksDetailsView.get_permalink()
        node.node_attrs["isLazy"] = True
        node.node_attrs["lazyLoadingUrl"] = DiskNodesJSONView.get_permalink()
        return self.render_to_response(node.node_attrs)


class DiskNodesJSONView(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        children = []

        basic_disks_parent_node = DynatreeNode()
        self._set_disk_container_node_attrs(Disk, basic_disks_parent_node)

        multipath_disks_parent_node = DynatreeNode()
        self._set_disk_container_node_attrs(MultipathDisk, multipath_disks_parent_node)

        for disk in Disk.objects.all():
            self._set_disk_node_attrs(disk, basic_disks_parent_node)
        children.append(basic_disks_parent_node.node_attrs)

        for disk in MultipathDisk.objects.all():
            self._set_disk_node_attrs(disk, multipath_disks_parent_node)
        children.append(multipath_disks_parent_node.node_attrs)

        return self.render_to_response(children)

    @classmethod
    @permalink
    def get_permalink(self):
        return ('disk_root_children_nodes', [])

    def _set_disk_container_node_attrs(self, model, container_node):
        container_node.node_attrs['title'] = model.get_node_title()
        container_node.node_attrs['url'] = model.get_list_url()
        container_node.node_attrs['isFolder'] = True

    def _set_disk_node_attrs(self, disk, parent_node):
        node_child = DynatreeNode()
        node_child.node_attrs['title'] = disk.name
        node_child.node_attrs['icon'] = 'hard_disk_32x32.png'
        node_child.node_attrs['url'] = disk.get_absolute_url()
        node_child.node_attrs['isFolder'] = True
        node_child.node_attrs['isLazy'] = True,
        node_child.node_attrs['lazyLoadingUrl'] = disk.get_children_lazy_loading_url()
        if parent_node.node_attrs['children'] is None:
            parent_node.node_attrs['children'] = []
        parent_node.node_attrs['children'].append(node_child.node_attrs)


class DiskChildrenNodesBaseView(JSONResponseMixin, View):

    model = None

    def get(self, request, disk_id, *args, **kwargs):
        objects = self.model.objects.filter(parent=disk_id)
        if len(objects) > 0:
            children = []
            #if not request.user.is_anonymous():
            node = DynatreeNode()
            node.node_attrs['title'] = self.model.get_node_title()
            node.node_attrs['isFolder'] = True
            node.node_attrs['isLazy'] = False
            node.node_attrs['url'] = objects[0].get_list_url()
            node.node_attrs['children'] = []
            for obj in objects:
                node_child = DynatreeNode()
                node_child.node_attrs['title'] = obj.name
                node_child.node_attrs['url'] = obj.get_absolute_url()
                node_child.node_attrs['isFolder'] = False
                node.node_attrs['children'].append(node_child.node_attrs)
            children.append(node.node_attrs)
        else:
            #Node has no children
            children = None

        return self.render_to_response(children)


class PartitionNodesJSONView(DiskChildrenNodesBaseView):
    model = Partition


class PathNodesJSONView(DiskChildrenNodesBaseView):
    model = Path
