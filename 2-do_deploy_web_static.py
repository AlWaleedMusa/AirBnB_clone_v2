#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
contents of the web_static folder of AirBnB Clone repo
using the function do_pack"""

from fabric.api import local, env, put, run
from datetime import datetime
import os


env.hosts = ["35.153.232.142", "100.25.130.239"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to your web servers, using the function do_deploy."""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_name_no_exist = file_name.split(".")[0]
        path_no_exist = "/data/web_static/releases/{}".format(file_name_no_exist)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_exist))
        run("tar -xzf /tmp/{} -C {}/".format(file_name, path_no_exist))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(path_no_exist, path_no_exist))
        run("rm -rf {}/web_static".format(path_no_exist))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_no_exist))
        return True
    except Exception as e:
        print(e)
        return False
