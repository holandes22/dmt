import os
import json

from django.db.models import get_model
from django.http import HttpResponse
from dmt.disks.models import Disk, MultipathDisk, Partition, Path

class DynatreeNode(object):
    """
    Attrs taken from the dynatree node docs, translated to python dict (e.g null = None, false = False)
    """
    def __init__(self):
        self.node_attrs = {
                         'title': None,
                         'key': None,
                         'isFolder': False,
                         'isLazy': False,
                         'tooltip': None,
                         'icon': None,
                         'addClass': None,
                         'noLink': False,
                         'activate': False,
                         'focus': False,
                         'expand': False,
                         'select': False,
                         'hideCheckbox': False,
                         'unselectable': False,
                         'children': None,
                        }

#This is the root tree
disk_tree_data = [
    {
     "title": "Disks", 
     "isFolder": True, 
     "key": "disks_root_node", 
     "url": "/objects/disks", 
     "isLazy": True,
     "lazyLoadingUrl": "/tree/disk_tree_disks_nodes/",
     },
]


def disk_tree_root(request):
    return HttpResponse(json.dumps(disk_tree_data))

def disk_tree_disks_nodes(request):
    children = []
    #if not request.user.is_anonymous():
    basic_disks = Disk.objects.all()
    mp_disks = MultipathDisk.objects.all()
    for basic_disk in basic_disks:
        node = DynatreeNode()
        node.node_attrs['title'] = "Basic disks"
        node.node_attrs['url'] = "/todo"
        node.node_attrs['isFolder'] = True
        
        node_child = DynatreeNode()
        node_child.node_attrs['title'] = basic_disk.name
        node_child.node_attrs['url'] = "/todo"
        node_child.node_attrs['isFolder'] = True
        node_child.node_attrs['isLazy'] = True,
        node_child.node_attrs['lazyLoadingUrl'] = os.path.join("/", "tree", "disk", str(basic_disk.id), "partition_nodes")
        node.node_attrs['children'] = [node_child.node_attrs]
        children.append(node.node_attrs)

    for mp_disk in mp_disks:
        node = DynatreeNode()
        node.node_attrs['title'] = "Multipath disks"
        node.node_attrs['url'] = "/todo"
        node.node_attrs['isFolder'] = True
        
        node_child = DynatreeNode()
        node_child.node_attrs['title'] = mp_disk.name
        node_child.node_attrs['url'] = "/todo"
        node_child.node_attrs['isFolder'] = True
        node_child.node_attrs['isLazy'] = True,
        node_child.node_attrs['lazyLoadingUrl'] = "/tree/mp_disk/path_nodes/",
        node.node_attrs['children'] = [node_child.node_attrs]
        children.append(node.node_attrs)
        
    return HttpResponse(json.dumps(children))

def generic_container_nodes(request, disk_id, model_name):
    children = []
    #if not request.user.is_anonymous():
    model = get_model("disks", model_name)
    node = DynatreeNode()
    node.node_attrs['title'] = model._meta.verbose_name_plural.title()
    node.node_attrs['url'] = "/todo"
    node.node_attrs['isFolder'] = True
    node.node_attrs['isLazy'] = False,
    node.node_attrs['children'] = []
    partitions = model.objects.filter(parent = disk_id)
    for partition in partitions:
        node_child = DynatreeNode()
        node_child.node_attrs['title'] = partition.name
        node_child.node_attrs['url'] = "/todo/get_from_model_url"
        node_child.node_attrs['isFolder'] = False
        node.node_attrs['children'].append(node_child.node_attrs)
    children.append(node.node_attrs)
    return HttpResponse(json.dumps(children))