Developement
------------

* Clone the repo
* Activate virtualenv and cd to the root of the repo
* pip install -r requirements-dev.txt
* Ensure that dmtcore is in the PYTHONPATH as well as dmt (better to add to virtualenv activate script)
* Add commands to be run as sudo for the dev user::

  <user>   ALL=NOPASSWD:/sbin/fdisk,/sbin/blkid,/sbin/multipath (plus all the necessary commands)
  Make sure this line is added after %admin ALL=(ALL) ALL and %sudo ALL=(ALL:ALL) ALL
  Make a backup copy of sudoers before editing

* django syncdb
* Run celeryd start
* Run python manage runserver (or cherrypy)

