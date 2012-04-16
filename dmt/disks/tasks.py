from celery.task import task
from dmtcore.disk import get_disks
from dmtcore.disk.base import BasicDisk
from dmtcore.disk.base import MultipathDisk as MultipathDiskObject
from dmt.disks.models import Disk, Partition, MultipathDisk

from django.core.exceptions import ObjectDoesNotExist

@task
def refresh_disk_models():
    # There must be an only instance of this task running at every given time
    # Find a way to lock it.
    # This is to  avoid situations of two different users forcing a refresh or
    # one user forcing a refresh a the same time the scheduler does

    # TODO: Make failsafe mechanism for uuid's. If for some reason dmtcore
    # cannot provide the uuid/wwid then this whole behaviour will lead to
    # erronuos information
    disks = get_disks()
    for disk in disks:
        if isinstance(disk, BasicDisk):
            try:
                db_disk = Disk.objects.get(disk_identifier = disk.disk_identifier)
            except ObjectDoesNotExist:
                db_disk = Disk()
            db_disk.name = disk.get_name()
            db_disk.filepath = disk.get_filepath()
            db_disk.disk_identifier = disk.disk_identifier
            db_disk.save()

            #now do the same for the partitions
            for partition in disk.get_partitions():
                if partition.get_uuid() is None:
                    continue
                try:
                    part = Partition.objects.get(uuid = partition.get_uuid())
                except ObjectDoesNotExist:
                    part = Partition()
                part.name = partition.get_name()
                part.uuid = partition.get_uuid()
                part.parent = db_disk
                part.save()
        else:
            db_mpdisk = MultipathDisk.objects.get(wwid = disk.wwid)
