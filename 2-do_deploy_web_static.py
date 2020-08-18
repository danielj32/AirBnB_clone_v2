from fabric.api import *
from datetime import datetime
import os
env.hosts = ['34.74.176.42', '34.75.43.152']
env.user = 'ubuntu'

def do_deploy(archive_path):
        """deploy to servers """
        if not os.path.exists(archive_path):
            return False

        filname = archive_path.split("/")
        filname = filname[1]
        f_name = filname.split('.')
        f_name = fname[0]
        
        n_path = '/data/web_static/releases/{}/'.format(f_name)
        
        try:
            put(archive_path, "/tmp/")
            run("mkdir -p {}".format(n_path))
            run("tar -xzf /tmp/{} -C {}".format(filname, n_path))
            run("rm /tmp/{}".format(filname))
            run("mv {}web_static/* {}".format(n_path, n_path))
            run("rm -rf {}web_static".format(n_path))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(n_path))
            return True
        except:
            return False
