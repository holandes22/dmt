import os
from django.db import models

class Disk(models.Model):

    name = models.CharField(max_length = 180)
    filepath = models.CharField(max_length = 200)
    devno = models.CommaSeparatedIntegerField(max_length = 100)
    disk_identifier = models.CharField(max_length = 200)
    
    def get_node_title(self):
        return "Basic disks"
    
    def get_children_lazy_loading_url(self):
        return os.path.join("/", "tree", "disk", str(self.id), "partition_nodes")


class Partition(models.Model):

    name = models.CharField(max_length = 180)
    devno = models.CommaSeparatedIntegerField(max_length = 100)
    parent = models.ForeignKey(Disk)
    uuid = models.CharField(max_length = 200)


class MultipathDisk(models.Model):

    name = models.CharField(max_length = 180)
    filepath = models.CharField(max_length = 200)
    wwid = models.CharField(max_length = 200)
    
    def get_node_title(self):
        return "Multi-path disks"
    
    def get_children_lazy_loading_url(self):
        return os.path.join("/", "tree", "disk", str(self.id), "path_nodes")


class Path(models.Model):

    name = models.CharField(max_length = 180)
    state = models.BooleanField()
    parent = models.ForeignKey(MultipathDisk)


