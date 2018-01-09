Django Debug Toolbar
--------------------

The Django Debug Toolbar will give you visibility into what django is spending time on during slower requests.

## Basic Outline

1. Install the django debug toolbar
    1. You can use the `debug_toolbar` branch to get the configurations customized for saleor

        ```bash
        ubuntu@saleor:~$ cd ~/saleor
        ubuntu@saleor:~$ git checkout debug_toolbar
        ubuntu@saleor:~$ pip3 install -r requirements.txt
        ```

1. Configure uwsgi to allow your browser to use the debug toolbar
    1. Find your IP (http://www.whatsmyip.org/)
    1. Edit `/etc/uwsgi/vassals/saleor_uwsgi.ini` in sudo mode.
    1. Add this line to the bottom:

        ```
        env = INTERNAL_IPS=<your IP here>
        ```

    1.  Restart uwsgi

        ```bash
        sudo supervisorctl restart uwsgi
        ```

1. Open a browser to saleor and navigate the site.  The django debug toolbar should appear as sidebar.

Full docs [here](https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#)

__Note: Running the server in debug mode will result in reduced performance__
