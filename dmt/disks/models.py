import os
from django.db import models

class BaseObject(models.Model):
    
    name = models.CharField(max_length = 180) 
    
    class Meta:
        abstract = True
        
    def get_model_attrs(self, filter_fields = ['id', 'pk', 'parent']):
        for field in self._meta.fields:
            if field.name not in filter_fields:
                if field.choices:
                    yield field.name, getattr(self, 'get_%s_display' % field.name)
                else:
                    yield field.name, getattr(self, field.name)


class Disk(BaseObject):
    
    filepath = models.CharField(max_length = 200)
    devno = models.CommaSeparatedIntegerField(max_length = 100)
    disk_identifier = models.CharField(max_length = 200)
    
    @models.permalink
    def get_absolute_url(self):
        return ('basic_disk_detail', [str(self.pk)])

    @classmethod
    @models.permalink
    def get_list_url(self):
        return ('basic_disk_list', [])
    
    @classmethod
    def get_node_title(self):
        return 'Basic disks'
    
    def get_children_lazy_loading_url(self):
        return os.path.join('/', 'tree', 'disk', str(self.pk), 'partition_nodes')


class Partition(BaseObject):

    devno = models.CommaSeparatedIntegerField(max_length = 100)
    parent = models.ForeignKey(Disk)
    uuid = models.CharField(max_length = 200)

    verbose_name_plural = "Partitions"
    
    @models.permalink
    def get_list_url(self):
        return ('partition_list', [str(self.parent.pk)])    

    @models.permalink
    def get_absolute_url(self):
        return ('partition_detail', [str(self.pk)])

    @classmethod
    def get_node_title(self):
        return 'Partitions'    


class MultipathDisk(BaseObject):

    filepath = models.CharField(max_length = 200)
    wwid = models.CharField(max_length = 200)

    @models.permalink
    def get_absolute_url(self):
        return ('multipath_disk_detail', [str(self.pk)])

    @classmethod
    @models.permalink
    def get_list_url(self):
        return ('multipath_disk_list', [])
           
    @classmethod
    def get_node_title(self):
        return 'Multipath disks'
    
    def get_children_lazy_loading_url(self):
        return os.path.join('/', 'tree', 'disk', str(self.pk), 'path_nodes')


class Path(BaseObject):

    state = models.BooleanField()
    parent = models.ForeignKey(MultipathDisk)

    @models.permalink
    def get_list_url(self):
        return ('path_list', [str(self.parent.pk)])    

    @models.permalink
    def get_absolute_url(self):
        return ('path_detail', [str(self.pk)])
    
    @classmethod
    def get_node_title(self):
        return 'Paths'    

