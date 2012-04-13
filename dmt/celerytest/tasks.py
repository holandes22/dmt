from celery.task import task
from dmtcore.disk import get_disks

@task
def list_disks_task():
    return get_disks()
