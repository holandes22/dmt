from django.contrib import admin
from dmt.disks.models import Disk, MultipathDisk, Partition, Path

admin.site.register(Disk)
admin.site.register(MultipathDisk)
admin.site.register(Partition)
admin.site.register(Path)